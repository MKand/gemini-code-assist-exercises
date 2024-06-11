import os
from flask import Flask, render_template
from client import GeminiImageClient

app = Flask(__name__)
app.config['TEMPLATE_FOLDER'] = 'templates'  # Add this line

# Function that takes an image path, resizes the image to be 200px wide while maintaining aspect ratio and stores it back in the original location


def create_image_captions():
    server_url = os.environ.get("SERVER_URL")
    folder_path = "images"

    if not project_id:
        raise ValueError("Environment variable for project id not set.")

    client = GeminiImageClient(server_url)
    image_captions = {}

    # Get JPEG images from the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            image_path = os.path.join(folder_path, filename)
            try:
                caption = client.generate_caption(image_path, "Write a caption for this image.")
                image_captions[filename] = caption  # Store filename as key
            except Exception as e:
                print(f"Error processing {image_path}: {e}")

    return image_captions

@app.route("/", methods=["GET"])
def index():
        image_captions = create_image_captions() 
        return render_template("./index.html", image_captions=image_captions)
    

if __name__ == "__main__":
    app.run(debug=True) 