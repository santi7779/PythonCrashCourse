filename = 'moby_dick.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry the file {filename} does not exist.")
else:
    words = contents.split()
    number_of_whales = words.count('the')
    print(number_of_whales)
