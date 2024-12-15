import os
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from typing import List, Tuple, Dict
import gradio as gr
from google.generativeai import GenerativeModel, configure, types

# Configure the Google Generative AI API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
configure(api_key=GOOGLE_API_KEY)

# MyApp class to handle PDFs and vector search
class MyApp:
    def __init__(self) -> None:
        self.documents = []
        self.embeddings = None
        self.index = None
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def load_pdfs(self, file_paths: List[str]) -> None:
        """Extracts text from multiple PDF files and stores them."""
        self.documents = []
        for file_path in file_paths:
            doc = fitz.open(file_path)
            for page_num in range(len(doc)):
                page = doc[page_num]
                text = page.get_text()
                self.documents.append({"file": file_path, "page": page_num + 1, "content": text})
        print("PDFs processed successfully!")

    def build_vector_db(self) -> None:
        """Builds a vector database using the content of the PDFs."""
        if not self.documents:
            print("No documents to process.")
            return
        contents = [doc["content"] for doc in self.documents]
        self.embeddings = self.model.encode(contents, show_progress_bar=True)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(np.array(self.embeddings))
        print("Vector database built successfully!")

    def search_documents(self, query: str, k: int = 3) -> List[Dict]:
        """Searches for relevant document snippets using vector similarity."""
        if not self.index:
            print("Vector database is not built.")
            return []
        query_embedding = self.model.encode([query], show_progress_bar=False)
        D, I = self.index.search(np.array(query_embedding), k)
        results = [self.documents[i] for i in I[0]]
        return results if results else [{"content": "No relevant documents found."}]

# Create an instance of MyApp
app = MyApp()

# Gradio functions
def upload_files(files) -> str:
    file_paths = [file.name for file in files]
    app.load_pdfs(file_paths)
    return f"Uploaded {len(files)} files successfully."

def build_vector_db() -> str:
    app.build_vector_db()
    return "Vector database built successfully!"

def respond(message: str, history: List[Tuple[str, str]]) -> Tuple[List[Tuple[str, str]], str]:
    # Retrieve relevant documents
    retrieved_docs = app.search_documents(message)
    context = "\n".join(
        [f"File: {doc['file']}, Page: {doc['page']}\n{doc['content'][:300]}..." for doc in retrieved_docs]
    )  # Trimming content for brevity

    # Generate response using the generative model
    model = GenerativeModel("gemini-2.0-flash-exp")
    generation_config = types.GenerationConfig(
        temperature=0.7,
        max_output_tokens=1024,
    )
    
    try:
        # The context is used as part of the prompt for the generative model
        response = model.generate_content([f"Context:\n{context}\n\nQuestion:\n{message}"], generation_config=generation_config)
        response_content = response.text if hasattr(response, "text") else "No response generated."
    except Exception as e:
        response_content = f"An error occurred while generating the response: {str(e)}"

    # Append the message and generated response to the chat history
    history.append((message, response_content))
    return history, ""

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# PDF Chatbot Powered by Gemini 2.0")
    gr.Markdown("Upload your PDFs, build a vector database, and start querying your documents.")

    with gr.Row():
        with gr.Column():
            upload_btn = gr.File(label="Upload PDFs", file_types=[".pdf"], file_count="multiple")
            upload_message = gr.Textbox(label="Upload Status", lines=2)
            build_db_btn = gr.Button("Build Vector Database")
            db_message = gr.Textbox(label="DB Build Status", lines=2)

            upload_btn.change(upload_files, inputs=[upload_btn], outputs=[upload_message])
            build_db_btn.click(build_vector_db, inputs=[], outputs=[db_message])

        with gr.Column():
            chatbot = gr.Chatbot(label="Chat Responses")
            query_input = gr.Textbox(label="Enter your query here")
            submit_btn = gr.Button("Submit")
            submit_btn.click(respond, inputs=[query_input, chatbot], outputs=[chatbot, query_input])

# Launch the Gradio app
demo.launch()
