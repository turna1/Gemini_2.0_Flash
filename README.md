# Let's build with Gemini 2.0 Flash 
**by: Rahatara Ferdousi**

This repository contains Jupyter notebooks that serve as starter guides for working with Gemini 2.0. These notebooks provide examples and templates for spatial and general tasks to help you get started quickly.
Gemini 2.0 is Google's latest large language model (LLM), succeeding the original Gemini. It's designed to be multimodal, meaning it can understand and operate across different types of information like text, code, images, audio, and video.


![image](https://github.com/user-attachments/assets/4935c8e1-3fc8-410f-8f75-60ed0ea0749c)



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



## Notebooks Included

### 1. **Gemini 2.0 Spatial Starter**
   File: `gemini2_0_spatial_starter.ipynb`
   
   - **Description**: This notebook demonstrates spatial capabilities in Gemini 2.0, focusing on handling image data..
   - **Key Features**:
     - Spatial data handling
     - Use-Cases of spatial analysis with Bounding Box 

### 2. **Gemini 2.0 Starter**
   File: `gemini_2_0_starter.ipynb`
   
   - **Description**: This notebook provides a general-purpose introduction to Gemini 2.0, showcasing its core features and functionality for a variety of tasks.
   - **Key Features**:
     - Introduction to Gemini 2.0 new capabilities like Google Search, Chat with Youtube Video
     - Basic examples of AI-driven workflows



## How to Use

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/gemini-2.0-notebooks.git
   ```

2. Navigate to the directory:
   ```bash
   cd gemini-2.0-notebooks
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Open the notebooks in Jupyter Notebook or JupyterLab:
   ```bash
   jupyter notebook
   ```

## Prerequisites

- Python 3.7 or higher
- Jupyter Notebook or JupyterLab

## Contributing

If you have ideas for improving these notebooks or adding more examples, feel free to fork the repository and submit a pull request.

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

## Support

For any questions or issues, please open an issue in this repository or reach out to the maintainer rferd068@uottawa.ca.
