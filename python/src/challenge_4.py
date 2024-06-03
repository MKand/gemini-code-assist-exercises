import json
import os

def transform_data(file_path):
  """
  Transforms the JSON data into the desired format and saves it to a new file.

  Args:
    file_path: Path to the input JSON file.
  """
  try:
    with open(file_path, 'r') as f:
      data = json.load(f)

    transformed_data = []
    for i, location in enumerate(data["locations"]):
      region_data = {
          "region": location["name"],
          "mayor": location["mayor"],
          "crime_rate": location["crime_rate"],
          "landmark": location["landmark"],
          "superheroes": data["superheroes"][i * 2: (i + 1) * 2],  # Split superheroes evenly
          "villains": data["villains"][i * 3: (i + 1) * 3]  # Split villains evenly
      }
      transformed_data.append(region_data)

    # Save the transformed data to a new file
    output_file_path = os.path.join(os.path.dirname(file_path), "file2.json")
    with open(output_file_path, 'w') as f:
      json.dump(transformed_data, f, indent=4)

    print(f"Transformed data saved to {output_file_path}")

  except FileNotFoundError:
    print(f"Error: File not found at '{file_path}'.")
  except json.JSONDecodeError:
    print(f"Error: Invalid JSON format in file '{file_path}'.")

if __name__ == "__main__":
  # Construct the relative path to the JSON file
  current_dir = os.path.dirname(os.path.abspath(__file__))
  json_file_path = os.path.join(current_dir, '..', 'data', 'file.json')

  transform_data(json_file_path)
