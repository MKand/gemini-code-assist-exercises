import argparse
import json


def load_and_validate_json(file_path):
    """
  Loads a JSON file and validates its structure.

  Args:
    file_path: Path to the JSON file.

  Returns:
    A dictionary containing the JSON data if valid, otherwise None.
  """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        # Validate the structure of the JSON data
        if not isinstance(data, dict):
            print("Error: JSON data must be a dictionary.")
            return None
        return data
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{file_path}'.")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load and validate JSON data.")

    args = parser.parse_args()
    data = load_and_validate_json(args.file)
    if data:
        print("JSON data loaded and validated successfully!")
    else:
        print("Failed to load and validate JSON data.")

