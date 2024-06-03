You can choose to do all the challenges in one python module or use multiple modules.

### Challenge 1:
1. Create your first python app that takes the name of the json file as a command line argument and loads it.
2. Print the name of the json file. The file should passed using the --file command line argument.
3. Validate the json strucure.

### Challenge 2:
Do some data filtering
1. Add another command line argument called "magic" that prints all the superheros that have magic as a superpower
1. [OPTIONAL] Make this a generic filter that searches for a specific superpower (example: superheros that have *super speed* as a superpower)

### Challenge 3:
REGEX transformation
1. Print out the phone numbers of all the super villans with their names.
2. You will see that the phone numbers have a different formats. We want to normalize them. Write a function that uses a regex expression to extract the digits of the number and then print them all out in the *(abc) def-ghij* format
3. We want to make sure the regex transformation works. Write a unit test that tests the function, with successes for the following test-cases "(555) 111-2222", "(555) 1234567", "555 222-2222", "555-333 4444", "555 666 7777", "4556660777".

#### Challenge 4:
Data transformation:
1. We've decided to split up the superheros and villans based on region. So, the first 2 superheros and the first 3 villans operate in region 1, whereas the remainder operate in region 2. We want to transform the data format so that it looks like this. 
```json 
[
    {
        region: name,
        mayor: name,
        crime_rate: value,
        landmark: value,
        superheroes: [
        ],
        villains: [
        ]
    },
    
]
```
Write a function that takes the current input file and transforms it into the desired format and saves it to a new file called file2.json in the same directory as file1.json


Task 1: Load and Validate the JSON Data

Provide the File Path:
Ask participants to enter the file path (or provide a sample file) of the JSON data to be transformed.
Use Gemini to generate code that reads the file contents and parses it as JSON.
Validate the Structure:
Use Gemini to suggest a function that checks if the JSON data conforms to the expected structure (e.g., contains the "superheroes," "villains," and "locations" keys).
If the data is invalid, display an error message to the user.
Task 2: Choose Transformations from the Menu

Display the Menu:
Present a clear, numbered menu listing all available transformations:
Basic transformations (filtering, renaming, adding/removing fields, sorting, data type conversion)
Regex Power-Ups
Get User Input:
Ask participants to select the desired transformation by entering the corresponding number.
For transformations that require additional parameters (e.g., filter criteria, regex patterns), prompt the user for input.
Task 3: Apply Transformations

Basic Transformations:
Use Gemini to generate code that implements the selected transformation based on user input.
For example, if the user selects "Filter by superhero power," Gemini could suggest code to filter the "superheroes" list based on the specified power.
Regex Power-Ups:
For tasks like search/replace or extraction, guide the participants to formulate a regex pattern. If they're stuck, use Gemini to suggest a pattern.
Use Gemini to generate code that applies the regex pattern to the relevant fields in the JSON data.
Task 4: Export the Transformed Data

Save or Display:
Ask participants if they want to save the transformed data to a new file or display it on the screen.
Implement Output:
Use Gemini to generate code that either writes the transformed data to a new file or prints it in a formatted way to the console.
Verify Results:
Encourage participants to review the output to ensure the transformations were applied correctly.