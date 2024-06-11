import base64
import requests
import os

class GeminiImageClient:
    """A client for interacting with the Gemini image processing Cloud Function."""

    def __init__(self, url):
        """Initializes the client with project ID and location."""
        self.project_id = project_id
        self.location = location
        self.cloud_function_url = f"${url}/server"

    def generate_caption(self, image_path, prompt):

        # Load the image
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            encoded_image = base64.b64encode(image_data).decode("utf-8")

        # Create the request data
        data = {"image": encoded_image, "prompt": prompt}

        # Send the POST request
        response = requests.post(self.cloud_function_url, data=data)

        # Check for errors
        if response.status_code != 200:
            raise Exception(f"Error processing image: {response.text}")

        # Return the generated text
        return response.json()["text"]

