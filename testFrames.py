import json

# Open and read the JSON file
with open('testFrames.json', 'r') as json_file:
    data = json.load(json_file)

second_info = data[1]

# Access the values in the JSON data
name = second_info['name']
age = second_info['pfp']
city = second_info['rectangleWidth']

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

#this is how we could store the moveset lol but kinda troll but works
code = """
def greet(name):
    print(f"Hello, {name}!")
print("hello world")
"""

exec(code)

# greet("Alice")

variable_to_transfer = 42
