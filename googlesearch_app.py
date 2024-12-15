import os
import gradio as gr
from google import genai
from google.genai.types import GenerateContentConfig, GoogleSearch, Tool

# Initialize GenAI Client
API_KEY = os.getenv("GOOGLE_API_KEY")  # Ensure to set this in Hugging Face Secrets
client = genai.Client(api_key=API_KEY)
MODEL_ID = "gemini-2.0-flash-exp"  # Replace with your desired model ID

def google_search_query(question, use_web_search):
    try:
        # Generate the AI response without web search initially
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=question,
        )
        ai_response = response.text  # AI response as plain text

        if use_web_search:
            # If user selects web search, redefine the tool and generate response with web search
            google_search_tool = Tool(google_search=GoogleSearch())
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=question,
                config=GenerateContentConfig(tools=[google_search_tool]),
            )
            search_results = response.candidates[0].grounding_metadata.search_entry_point.rendered_content
        else:
            search_results = "Web search not used."

        return ai_response, search_results
    except Exception as e:
        return f"Error: {str(e)}", ""

# Gradio Interface using Chatbot and conditional web search
with gr.Blocks(theme=gr.themes.Glass(secondary_hue = "violet")) as app:
    gr.Markdown("# Gemini 2.0 Google Search Custom UI")
    with gr.Row(): 
        chatbot = gr.Chatbot(label="Chatbot Responses")
    with gr.Row():
        question_input = gr.Textbox(lines=2, label="Ask a Question")
        web_search_checkbox = gr.Checkbox(label="Enhance with Web Search", value=False)
    with gr.Row():
        submit_button = gr.Button("Submit")
    
    def update_chatbot(question, use_web_search, chat_log):
        ai_response, search_results = google_search_query(question, use_web_search)
        chat_log.append(("You", question))
        chat_log.append(("AI", ai_response))
        if use_web_search:
            chat_log.append(("AI + Web Search", search_results))
        return chat_log
    
    submit_button.click(
        fn=update_chatbot,
        inputs=[question_input, web_search_checkbox, chatbot],
        outputs=[chatbot]
    )

app.launch()
