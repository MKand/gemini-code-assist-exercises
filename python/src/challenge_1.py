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

def filter_superheroes_by_magic(data):
  """
  Filters superheroes with magic powers from the given JSON data.

  Args:
    data: A dictionary containing the JSON data.

  Returns:
    A list of superheroes with magic powers.
  """
  if not isinstance(data, dict):
    raise ValueError("Invalid JSON data format.")
  if "superheroes" not in data:
    raise ValueError("Missing 'superheroes' key in JSON data.")

  magic_heroes = [hero for hero in data["superheroes"] if "magic" in hero["powers"]]
  return magic_heroes

def filter_superheroes_by_power(data, superpower):
  """
  Filters superheroes with a specific superpower from the given JSON data.

  Args:
    data: A dictionary containing the JSON data.
    superpower: The superpower to filter for.

  Returns:
    A list of superheroes with the specified superpower.
  """
  if not isinstance(data, dict):
    raise ValueError("Invalid JSON data format.")
  if "superheroes" not in data:
    raise ValueError("Missing 'superheroes' key in JSON data.")

  filtered_heroes = [hero for hero in data["superheroes"] if superpower in hero["powers"]]
  return filtered_heroes

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Load and validate JSON data.")
  parser.add_argument("--magic", action="store_true", help="Print superheroes with magic powers.")
  parser.add_argument("--power", help="Superpower to filter for.")

  args = parser.parse_args()
  data = load_and_validate_json(args.file)
  if data:
    print("JSON data loaded and validated successfully!")
    if args.magic:
      magic_heroes = filter_superheroes_by_magic(data)
      print("Superheroes with magic powers:")
      for hero in magic_heroes:
        print(hero["name"])
    if args.power:
      filtered_heroes = filter_superheroes_by_power(data, args.power)
      print(f"Superheroes with the '{args.power}' superpower:")
      for hero in filtered_heroes:
        print(f"- {hero['name']}")    
    # Further processing of the data can be done here
  else:
    print("Failed to load and validate JSON data.")
