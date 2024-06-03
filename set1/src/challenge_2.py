import argparse
import json
import os

print(os.getcwd())
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

def filter_superheroes(data, filters):
  """
  Filters superheroes based on the provided filters.

  Args:
    data: A dictionary containing the JSON data.
    filters: A dictionary of key-value pairs and logical operators for filtering.

  Returns:
    A list of superheroes that match the filters.
  """
  if not isinstance(data, dict):
    raise ValueError("Invalid JSON data format.")
  if "superheroes" not in data:
    raise ValueError("Missing 'superheroes' key in JSON data.")

  filtered_heroes = []
  for hero in data["superheroes"]:
    match = True
    for key, value in filters.items():
      if key not in hero:
        print(f"Warning: Filter key '{key}' not found in superhero data.")
        match = False
        break
      if isinstance(value, list):
        # Check if any of the values in the list match
        if any(v in hero[key] for v in value):
          continue
        else:
          match = False
          break
      else:
        # Check if the value matches
        if value in hero[key]:
          continue
        else:
          match = False
          break
    if match:
      filtered_heroes.append(hero)
  return filtered_heroes

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Load and validate JSON data.")
  parser.add_argument("--filter", help="Filter criteria in the format 'key1:value1,key2:value2,...'.")
  args = parser.parse_args()
  
  # Construct the relative path to the JSON file
  current_dir = os.path.dirname(os.path.abspath(__file__))
  json_file_path = os.path.join(current_dir, '..', 'data', 'file.json')

  data = load_and_validate_json(json_file_path)
  if data:
    if args.filter:
      filters = {}
      for filter_str in args.filter.split(","):
        key, value = filter_str.split(":")
        if "," in value:
          # Multiple values for the filter
          filters[key] = [v.strip() for v in value.split(",")]
        else:
          filters[key] = value.strip()
      filtered_heroes = filter_superheroes(data, filters)
      print(f"Superheroes matching the filters:")
      for hero in filtered_heroes:
        print(f"- {hero['name']}")
    # Further processing of the data can be done here
  else:
    print("Failed to load and validate JSON data.")

