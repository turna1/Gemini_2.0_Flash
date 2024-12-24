# Let's build with Gemini 2.0 Flash 
**by: Rahatara Ferdousi**

This repository contains **starter guides**, **code files**, and **Jupyter notebooks** to help you build **custom apps** and **user interfaces** leveraging [Google Gemini 2.0 Flash](https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/). 
I will periodically update on projects created using Gemini2.0 Flash.
I developed the apps with custom UI and modified the official starter notebooks in a beginner friendly manner.  
![image](https://github.com/user-attachments/assets/4935c8e1-3fc8-410f-8f75-60ed0ea0749c)

## **What’s Inside?**

1. **Project Links**
  i) **Project HiMa**- [A Multmodal Assistant for Maternity Support.](https://github.com/turna1/HiMa?tab=readme-ov-file)

1. **Custom UI for Spatial Understanding**
   ![image](https://github.com/user-attachments/assets/3710ec6b-b97b-4323-8dd9-233df12482f5)

   - A custom **Gradio-based application** that utilizes **Gemini 2.0** for spatial reasoning.  
   - **Files**:  
     - `spatial_app.py`  
     - `spatial_requirements.txt`  
   - Generates **labeled bounding boxes** and annotations for objects in images based on user input prompts.  
![image](https://github.com/user-attachments/assets/58082855-cf01-431f-a802-cfd6b01002ab)
![image](https://github.com/user-attachments/assets/a1ac75ea-19a9-4723-b96b-88a3285ee9da)

2. **Grounded Text Response Flexibility**  
   - A grounded response app that combines **Gemini 2.0 Flash** with **Google Search** to provide real-time, search-enhanced answers.
    ![image](https://github.com/user-attachments/assets/77356607-bdf4-4c91-86de-fd3b01678b58)
 
   - **Files**:  
     - `googlesearch_app.py`  
     - `googlesearch_requirements.txt`  ![image](https://github.com/user-attachments/assets/48ba9736-0889-40b2-a3ed-c457fc61f3fe)

   - Flexible for applications needing factual, grounded responses.
     

3. **Retrieval-Augmented Generation (RAG) App to Chat with Multiple PDFs**  
   - A RAG-based application that uses **Gemini 2.0 Flash** for retrieving knowledge from external sources (PDF) and offering retrieval with language generation.
     ![image](https://github.com/user-attachments/assets/bd4abe75-c6b8-472c-8651-6bea5d8b16aa)

   - **Files**:  
     - `rag_app.py`  
     - `rag_requirements.txt`  
   - Ideal for building apps that require dynamic information retrieval and accurate contextual responses.
4. **Starter Guides in Jupyter Notebooks**  
   - Ready-to-use **Jupyter notebooks** with practical examples for:  
     - **Spatial Tasks**: Image-based reasoning and object detection.  
       - File: `gemini2_0_spatial_starter.ipynb`  
     - **General Multimodal Tasks**: Text, image, and code understanding templates.  
       - File: `gemini2_0_starter.ipynb`
      
## **How to Use these resources**

### **1. Using the Applications (`app.py` and `requirements.txt`)**

#### **Option 1: Deploy on Hugging Face Spaces**  
1. **Rename Files**:  
   - Remove "spatial" or "google search" from the filenames for clarity.  
     - Example: Rename `spatial_app.py` → `app.py` and `spatial_requirements.txt` → `requirements.txt`.  
   - Do the same for `googlesearch_app.py` and `googlesearch_requirements.txt` if deploying the grounded text app.

2. **Upload to Hugging Face Spaces**:  
   - Create a new Space on [Hugging Face](https://huggingface.co/spaces).  
   - Upload the `app.py` and `requirements.txt` files.  
   - Hugging Face will automatically set up the environment and run the app.

3. **Run the App**:  
   - Once deployed, the app will be available at a shareable URL.  
   - Test it by uploading an image and providing input prompts.

---

#### **Option 2: Run Locally on Your Machine**  
1. **Set Up Your Environment**:  
   - Clone the repository:  
     ```bash
     git clone https://github.com/your-repo-url
     cd your-repo-folder
     ```

   - Install dependencies:  
     ```bash
     pip install -r requirements.txt
     ```

---
2. **Run the App**:  
   - For **Spatial App**:  
     ```bash
     python spatial_app.py
     ```  
   - For **Grounded Text App**:  
     ```bash
     python googlesearch_app.py
     ```

3. **Access the App**:  
   - Open your browser and navigate to:  
     ```
     http://127.0.0.1:7860
     ```  
   - Upload images, provide prompts, and test the app functionality.


### **2. Using the Jupyter Notebooks**  
To run the notebooks, use **Google Colab** for an interactive experience.

1. **Open the Notebook in Colab**:  
   - For **Spatial Tasks**:  
     - Open [`gemini2_0_spatial_starter.ipynb`](https://colab.research.google.com) in Colab.  
   - For **General Multimodal Tasks**:  
     - Open [`gemini2_0_starter.ipynb`](https://colab.research.google.com) in Colab.

2. **Follow Step-by-Step Instructions**:  
   - Run each cell in sequence.  
   - Follow the inline comments and guidance provided within the notebook.

3. **Test and Modify**:  
   - Modify prompts, upload images, or extend code examples to explore the capabilities of Gemini 2.0.  

---


# **Learn More about Gemini2.0**
Gemini 2.0 is Google's latest large language model (LLM), succeeding the original Gemini. It's designed to be multimodal, meaning it can understand and operate across different types of information like text, code, images, audio, and video.

*   **Multimodality:** This is a core feature. Gemini 2.0 aims to seamlessly integrate various data types, allowing for more complex and nuanced understanding and generation of content. For example, it could analyze an image and generate a detailed text description, or take a text prompt and create a corresponding image.
*   **Improved Reasoning and Coding:** Google has emphasized advancements in Gemini's reasoning abilities, making it better at problem-solving and logical deduction. It also shows improved performance in coding tasks, including generating, explaining, and debugging code in multiple programming languages.
*   **Scalability and Efficiency:** Like many modern LLMs, Gemini is designed to be scalable, meaning it can be deployed on various hardware and handle different workloads. Efficiency improvements mean it can potentially run faster and use fewer resources.
*   **Different Sizes:** Similar to other LLMs, Gemini comes in different sizes (Ultra, Pro, Nano) to balance performance and resource requirements. Ultra is the most powerful, while Nano is designed for on-device applications.

**Capabilities for Beginners:**

Imagine Gemini 2.0 as a very advanced assistant that can:

*   **Understand and generate text:** Write stories, poems, articles, summaries, translate languages, answer questions in a comprehensive way.
*   **Work with images:** Describe what's in a picture, create images from text descriptions, answer questions about images.
*   **Help with coding:** Write code in various programming languages, explain what code does, help find errors in code.
*   **Handle different types of information together:** For example, you could give it a picture and ask it to write a story about it, or ask it to create a piece of code based on a textual description and an example image.

Essentially, it's a versatile tool for various creative and practical tasks, going beyond just text-based interactions. It's designed to be more intuitive and capable by understanding and working with the world in a more holistic way, similar to how humans do.
Here are some of the most relevant and helpful links to learn more:

**Official Announcements and Blog Posts:**

*   **Google's Official Blog Post:** This is a good starting point, giving an overview of Gemini 2.0 and its key features:
    *   [https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/](https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/)
*   **Google Product Blog:** This post focuses more on the practical applications and how to access Gemini:
    *   [https://blog.google/products/gemini/google-gemini-ai-collection-2024/](https://blog.google/products/gemini/google-gemini-ai-collection-2024/)

**Technical Documentation and Developer Resources:**

*   **Vertex AI Documentation:** This is where you'll find technical details and how to use Gemini 2.0 through Google Cloud's Vertex AI platform:
    *   [https://cloud.google.com/vertex-ai/generative-ai/docs/gemini-v2](https://cloud.google.com/vertex-ai/generative-ai/docs/gemini-v2)
*   **Google AI Studio:** This is a platform where developers can experiment with Gemini and other AI models:
    *   [https://aistudio.google.com/](https://aistudio.google.com/)

**Other Useful Links:**

*   **YouTube Video Breakdown:** This video provides a comprehensive overview of Gemini 2.0 and related announcements:
    *   [https://www.youtube.com/watch?v=W08Jl6NzwiA](https://www.youtube.com/watch?v=W08Jl6NzwiA) 

Keep in mind that Gemini 2.0 is still being rolled out and improved, so information may change over time. These links should give you a solid foundation for understanding its capabilities and potential.


If You're looking for more hands-on experience with Gemini 2.0! Here are some GitHub repositories with Colab notebooks that will help you get started:

**1. Google Cloud Platform's Generative AI Samples:**

*   **Main Repository:** This is the central hub for Google's generative AI examples, including Gemini:
    *   [https://github.com/GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai)
*   **Gemini 2.0 Flash Intro:** This notebook provides a great introduction to using the Gemini API with the Gemini 2.0 Flash model. It covers various tasks like text generation, chat, multimodal data processing, and function calling:
    *   [https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_2_0_flash.ipynb](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_2_0_flash.ipynb)

**2. Google Gemini Cookbook:**

*   **Cookbook Repository:** This repository offers a collection of examples and guides for using the Gemini API:
    *   [https://github.com/google-gemini/cookbook](https://github.com/google-gemini/cookbook)
*   **Multimodal Live API Starter:** This notebook demonstrates how to use the Gemini 2.0 Multimodal Live API for real-time vision and audio streaming applications:
    *   [https://github.com/google-gemini/cookbook/blob/main/gemini-2/live_api_starter.ipynb](https://github.com/google-gemini/cookbook/blob/main/gemini-2/live_api_starter.ipynb)

**Key things to note when using these Colab notebooks:**

*   **API Keys:** You'll need to set up an API key to access the Gemini API. The notebooks usually provide instructions on how to do this, often involving creating a Colab Secret.
*   **Installation:** You'll likely need to install the `google-genai` Python SDK. This is usually done with a simple `!pip install` command within the Colab notebook.
*   **Authentication:** You might need to authenticate your Colab environment to access Google Cloud resources.

These resources should provide you with a good starting point for experimenting with Gemini 2.0 in Colab. They offer practical examples and cover various aspects of the API, allowing you to explore its capabilities firsthand.

If you have ideas for improving these notebooks or adding more examples, feel free to fork the repository and submit a pull request.

## Support

For any questions or issues, please open an issue in this repository or reach out to the maintainer rferd068@uottawa.ca.
