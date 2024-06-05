import base64
import requests
import io
from PIL import Image

class GeminiImageClient:
    """A client for interacting with the Gemini image processing Cloud Function."""

    def __init__(self, project_id, location):
        """Initializes the client with project ID and location."""
        self.project_id = project_id
        self.location = location
        self.cloud_function_url = f"https://{location}-{project_id}.cloudfunctions.net/server"

    def generate_caption(self, image_path, prompt):

        # Load the image
        with open(image_path, "rb") as image_file:
            resized_image = self.resize_image(image_file) 
            resized_image_buffer = io.BytesIO() 
            resized_image.save(resized_image_buffer, format="JPEG") 
            encoded_image = base64.b64encode(resized_image_buffer.getvalue()).decode("utf-8")

        # Create the request data
        data = {"image": encoded_image, "prompt": prompt}

        # Send the POST request
        response = requests.post(self.cloud_function_url, data=data)

        # Check for errors
        if response.status_code != 200:
            raise Exception(f"Error processing image: {response.text}")

        # Return the generated text
        return response.json()["text"]

    # Function that takes an image and resizes it to be 200px wide while maintaining aspect ratio. 
    def resize_image(self, image_file, width=200):
        image = Image.open(image_file)
        original_width, original_height = image.size
        aspect_ratio = original_height / original_width
        new_height = int(width * aspect_ratio)
        resized_image = image.resize((width, new_height))
        return resized_image
