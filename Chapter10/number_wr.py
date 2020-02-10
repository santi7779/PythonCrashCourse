import json

favorite_number = input("What is your favorite number? ")
favorite_number = int(favorite_number)

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(favorite_number, f)

filename = 'numbers.json'
with open(filename) as f:
    favorite_number = json.load(f)

print(f"I know your favorite number it's {favorite_number}.")