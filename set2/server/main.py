import base64
import vertexai
import io
import os
import random
import string
from PIL import Image as im
from vertexai.generative_models import GenerativeModel, Part, Image
import vertexai.preview.generative_models as generative_models

import functions_framework

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")
vertexai.init(project=PROJECT_ID, location=LOCATION)
model = GenerativeModel(
    "gemini-1.5-flash-001",
  )
generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

@functions_framework.http
def process_image(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    if request.method == 'POST':
        # Get the image and prompt from the request
        image_data = request.form.get('image')
        prompt = request.form.get('prompt')

        random_image_name = generate_random_string(10) + ".jpg"

        # Decode the image data
        image_bytes = base64.b64decode(image_data)
        # Check if the image size is larger than 256 MB
        if len(image_bytes) > 256 * 1024 * 1024:
            return {'error': 'Image size exceeds 256 MB limit.'}, 400
        image = im.open(io.BytesIO(image_bytes))

        image.save(random_image_name)
        part_img = Part.from_image(Image.load_from_file(random_image_name))

        response = generate(image_part=part_img, prompt=prompt)
        
        os.remove(random_image_name)

        # Return the processed image data as a JSON response
        return {'text': response}, 200
    else:
        return 'Only POST requests are allowed', 405

def generate_random_string(length):
    """Generates a random string of specified length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate(image_part, prompt):
  responses = model.generate_content(
      [image_part, prompt],
      generation_config=generation_config,
      safety_settings=safety_settings,
      stream=False,
  )
  return responses.text

