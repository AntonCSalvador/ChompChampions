import json

# Open and read the JSON file
with open('testFrames.json', 'r') as json_file:
    data = json.load(json_file)

second_info = data[1]

# Access the values in the JSON data
name = second_info['name']
age = second_info['age']
city = second_info['city']

# Print the values
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")

#if champ0 is clicked
    #player1 = data[0]
#or is it better to do 
#if champ0 is clicked
    #champ0 = data[0]

#get basically frame times
    #

#name = 

# source_file.py

variable_to_transfer = 42
