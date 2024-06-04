
# Challenge Set 1: Superheroes and Villains Data Challenges

Welcome to the Superheroes and Villains Data Challenges! In these challenges, you'll work with a JSON file containing information about superheroes, villains, and their locations. You'll use Python and Gemini Code Assist to complete tasks like data loading, filtering, formatting, and transformation.

Use the *set1* folder as your working directory.

## Challenge 1: Loading and Validating JSON Data

1. **Create a Python app:** Write a Python script that takes the name of a JSON file as a command-line argument and loads it.
2. **Print the file name:** Print the name of the JSON file that was loaded.
3. **Validate the JSON structure:** Ensure that the JSON data has the expected structure. Use the `--file` command-line argument to specify the JSON file.

**Example Usage:**

```bash
python challenge_1.py --file data/file.json
```

## Challenge 2: Data Filtering
1. Filter by magic: Add a command-line argument called --magic that prints all the superheroes who have "magic" as a superpower.
Example Usage:
```sh
python challenge_2.py --file data/file.json --magic
```
2. Generic filtering: Make the filtering more generic. Add a command-line argument called --filter that allows users to specify a property and value and prints all superheroes with those properties.
Example Usage:
```sh
python challenge_2.py --file data/file.json --filter powers:super-strength
```

## Challenge 3: Regular Expression Transformation
Print villain phone numbers: Print the names and phone numbers of all the super villains.
Format phone numbers: The phone numbers in the JSON file have different formats. Write a Python function that uses a regular expression to extract the digits from the phone numbers and format them in the **(ddd) ddd-dddd** format.
Unit testing: Write unit tests to ensure that your phone number formatting function works correctly for various valid and invalid phone number formats.
Example Test Cases:
- (555) 111-2222
- (555) 1234567
- 555 222-2222
- 555-333 4444
- 555 666 7777
- 4556660777

## Challenge 4: Data Transformation
1. Region-based data: We want to split the superheroes and villains into regions. The first two superheroes and the first three villains belong to the first region, and the rest belong to second region
Transform the data: Transform the JSON data into a new format where each region is represented as a dictionary containing its name, mayor, crime rate, landmark, and lists of superheroes and villains.
2. Save the transformed data: Save the transformed data to a new JSON file called **file2.json** in the same directory as the original file.

Desired Output:

```json
[
    {
        "region": "Central City",
        "mayor": "Anthony Bellows",
        "crime_rate": 60,
        "landmark": "S.T.A.R. Labs",
        "superheroes": [
            {
                "name": "Captain Electro",
                "real_name": "Michael Faraday",
                "powers": ["electricity-manipulation", "super-speed", "energy-blasts"],
                "weakness": "water",
                "age": 35,
                "sidekick": "Sparky",
                "email": "captain.electro@example.com",
                "phone_number": "(555) 867-5309"
            },
            {
                "name": "The Amazing Arachnid",
                "real_name": "Cindy Moon",
                "powers": ["super-strength", "agility", "web-slinging"],
                "weakness": "insecticides",
                "age": 22,
                "sidekick": "none",
                "email": "amazing.arachnid@example.com",
                "phone_number": "(555) 123-4567"
            }
        ],
        "villains": [
            {
                "name": "The Joker",
                "real_name": "Unknown",
                "evil_plan": "Create chaos and anarchy",
                "henchmen": 10,
                "catchphrase": "Why so serious?",
                "email": "joker@example.com",
                "phone_number": "(555) 555-5555"
            },
            {
                "name": "Lex Luthor",
                "real_name": "Alexander Luthor",
                "evil_plan": "Destroy Superman",
                "henchmen": 500,
                "catchphrase": "Kneel before Zod!",
                "email": "lex.luthor@lexcorp.com",
                "phone_number": "555 222-2222"
            },
            {
                "name": "Madame Mischief",
                "real_name": "Harleen Quinzel",
                "evil_plan": "Spread chaos and mayhem",
                "henchmen": 2,
                "catchphrase": "Hee-yah!",
                "email": "madame.mischief@example.com",
                "phone_number": "555) 111-2222"
            }
        ]
    },
    {
        "region": "Star City",
        "mayor": "Oliver Queen",
        "crime_rate": 85,
        "landmark": "Queen Consolidated",
        "superheroes": [
            {
                "name": "Dr. Mystic",
                "real_name": "Stephen Strange",
                "powers": ["magic", "teleportation", "dimensional-travel"],
                "weakness": "his own arrogance",
                "age": 45,
                "sidekick": "Wong",
                "email": "dr.mystic@example.com",
                "phone_number": "(555)9876543"
            }
        ],
        "villains": [
            {
                "name": "The Penguin",
                "real_name": "Oswald Cobblepot",
                "evil_plan": "Control Gotham's underworld",
                "henchmen": 30,
                "catchphrase": "Waddle waddle!",
                "email": "penguin@example.com",
                "phone_number": "555-333 4444"
            },
            {
                "name": "Poison Ivy",
                "real_name": "Pamela Isley",
                "evil_plan": "Protect plant life at all costs",
                "henchmen": 0,
                "catchphrase": "Nature always wins!",
                "email": "poison.ivy@example.com",
                "phone_number": "555 666 7777"
            }
        ]
    }
]
```

# Challenge Set 2: 
