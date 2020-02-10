import json

favorite_number = input("What is your favorite number? ")
favorite_number = int(favorite_number)

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(favorite_number, f)



