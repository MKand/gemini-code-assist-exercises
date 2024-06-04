import os
from client import GeminiImageClient

def main():
    project_id = os.environ.get("PROJECT_ID", 'code-assist-demo')
    location = os.environ.get("LOCATION", "us-central1")
    folder_path = "../images"  
    client = GeminiImageClient(project_id, location)
    image_captions = {}

    # Get JPEG images from the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            image_path = os.path.join(folder_path, filename)
            try:
                caption = client.generate_caption(image_path, "Write a caption for this image.")
                image_captions[image_path] = caption
            except Exception as e:
                print(f"Error processing {image_path}: {e}")

    # Display images and captions using Matplotlib
    for image_path, caption in image_captions.items():
        print(f"Caption for {image_path}: {caption}")

if __name__ == "__main__":
    main()
