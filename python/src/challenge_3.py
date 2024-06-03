import json
import os
import re

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

def format_phone_number(phone_number):
  """
  Formats a phone number to (area code) numberpart1-numberpart2.

  Args:
    phone_number: The phone number to format.

  Returns:
    The formatted phone number, or None if the format is invalid.
  """
  # match = re.match(r'(\+?\d{1,3}\s*)?(\(?\d{3}\)?)?\s*(\d{3})[- ]*(\d{4})', phone_number)
  match = re.match(r'\(?(\d{3})\)?[\s\-]*(\d{3})[\s\-]*(\d{4})', phone_number)
  if match:
    area_code, numberpart1, numberpart2 = match.groups()
    result = f"({area_code}) {numberpart1}-{numberpart2}"
    return result
  else:
    print(f"Warning: Invalid phone number format {phone_number}.")
    return None

def print_villain_phone_numbers(data):
  """
  Prints the phone numbers of all super villains with their names.

  Args:
    data: A dictionary containing the JSON data.
  """
  if not isinstance(data, dict):
    raise ValueError("Invalid JSON data format.")
  if "villains" not in data:
    raise ValueError("Missing 'villains' key in JSON data.")

  for villain in data["villains"]:
    formatted_phone_number = format_phone_number(villain["phone_number"])
    if formatted_phone_number:
      print(f"Villain: {villain['name']}, Phone: {formatted_phone_number}")
    else:
      print(f"Villain: {villain['name']}, Phone: Invalid phone number format")


if __name__ == "__main__":
  # Construct the relative path to the JSON file
  current_dir = os.path.dirname(os.path.abspath(__file__))
  json_file_path = os.path.join(current_dir, '..', 'data', 'file.json')

  data = load_and_validate_json(json_file_path)
  if data:
    print_villain_phone_numbers(data)
  else:
    print("Failed to load and validate JSON data.")

