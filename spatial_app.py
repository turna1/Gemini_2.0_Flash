import gradio as gr
import os
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from PIL import ImageColor
import json
from google import genai
from google.genai import types

# Initialize Google Gemini client
client = genai.Client(api_key=os.environ['GEM_API_KEY'])
model_name = "gemini-2.0-flash-exp"

bounding_box_system_instructions = """
    Return bounding boxes as a JSON array with labels. Never return masks or code fencing. Limit to 25 objects.
    If an object is present multiple times, name them according to their unique characteristic (colors, size, position, unique characteristics, etc..).
"""

additional_colors = [colorname for (colorname, colorcode) in ImageColor.colormap.items()]

def parse_json(json_output):
    """
    Parse JSON output from the Gemini model.
    """
    lines = json_output.splitlines()
    for i, line in enumerate(lines):
        if line == "```json":
            json_output = "\n".join(lines[i+1:])  # Remove everything before "```json"
            json_output = json_output.split("```")[0]  # Remove everything after the closing "```"
            break
    return json_output

def plot_bounding_boxes(im, bounding_boxes):
    """
    Plots bounding boxes on an image with labels.
    """
    im = im.copy()
    width, height = im.size
    draw = ImageDraw.Draw(im)
    colors = [
        'red', 'green', 'blue', 'yellow', 'orange', 'pink', 'purple', 'cyan',
        'lime', 'magenta', 'violet', 'gold', 'silver'
    ] + additional_colors

    try:
        # Use a default font if NotoSansCJK is not available
        try:
            font = ImageFont.load_default()
        except OSError:
            print("NotoSansCJK-Regular.ttc not found. Using default font.")
            font = ImageFont.load_default()

        bounding_boxes_json = json.loads(bounding_boxes)
        for i, bounding_box in enumerate(bounding_boxes_json):
            color = colors[i % len(colors)]
            abs_y1 = int(bounding_box["box_2d"][0] / 1000 * height)
            abs_x1 = int(bounding_box["box_2d"][1] / 1000 * width)
            abs_y2 = int(bounding_box["box_2d"][2] / 1000 * height)
            abs_x2 = int(bounding_box["box_2d"][3] / 1000 * width)

            if abs_x1 > abs_x2:
                abs_x1, abs_x2 = abs_x2, abs_x1

            if abs_y1 > abs_y2:
                abs_y1, abs_y2 = abs_y2, abs_y1

            # Draw bounding box and label
            draw.rectangle(((abs_x1, abs_y1), (abs_x2, abs_y2)), outline=color, width=4)
            if "label" in bounding_box:
                draw.text((abs_x1 + 8, abs_y1 + 6), bounding_box["label"], fill=color, font=font)
    except Exception as e:
        print(f"Error drawing bounding boxes: {e}")

    return im

def predict_bounding_boxes(image, prompt):
    """
    Process the image and prompt through Gemini and draw bounding boxes.
    """
    try:
        # Resize the image for input
        image = image.resize((1024, int(1024 * image.height / image.width)))
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        image_bytes = buffered.getvalue()

        # Make API request to Gemini
        response = client.models.generate_content(
            model=model_name,
            contents=[prompt, image],
            config=types.GenerateContentConfig(
                system_instruction=bounding_box_system_instructions,
                temperature=0.5,
                safety_settings=[
                    types.SafetySetting(
                        category="HARM_CATEGORY_DANGEROUS_CONTENT",
                        threshold="BLOCK_ONLY_HIGH",
                    )
                ],
            )
        )

        print("Gemini response:", response.text)

        # Parse and plot bounding boxes
        bounding_boxes = parse_json(response.text)
        if not bounding_boxes:
            raise ValueError("No bounding boxes returned.")

        result_image = plot_bounding_boxes(image, bounding_boxes)
        return result_image
    except Exception as e:
        print(f"Error during processing: {e}")
        return image, f"Error: {e}"

def gradio_interface():
    """
    Gradio app interface for bounding box generation with example pairs.
    """
    # Example image + prompt pairs
    examples = [
        ["cookies.jpg", "Detect the cookies and label their types."],
        ["messed_room.jpg", "Find the unorganized item and suggest action in label in the image to fix them."],
        ["yoga.jpg", "Show the different yoga poses and name them."],
        ["zoom_face.png", "Label the tired faces in the image."]
    ]

    with gr.Blocks(gr.themes.Glass(secondary_hue= "rose")) as demo:
        gr.Markdown("# Gemini Bounding Box Generator")

        with gr.Row():
            with gr.Column():
                gr.Markdown("### Input Section")
                input_image = gr.Image(type="pil", label="Input Image")
                input_prompt = gr.Textbox(lines=2, label="Input Prompt", placeholder="Describe what to detect.")
                submit_btn = gr.Button("Generate")

            with gr.Column():
                gr.Markdown("### Output Section")
                output_image = gr.Image(type="pil", label="Output Image")
                #output_json = gr.Textbox(label="Bounding Boxes JSON")

        gr.Markdown("### Examples")
        gr.Examples(
            examples=examples,
            inputs=[input_image, input_prompt],
            label="Example Images with Prompts"
        )

        # Event to generate bounding boxes
        submit_btn.click(
            predict_bounding_boxes,
            inputs=[input_image, input_prompt],
            outputs=[output_image]
        )

    return demo



if __name__ == "__main__":
    app = gradio_interface()
    app.launch()
