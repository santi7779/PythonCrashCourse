filename = 'learning_python.txt'

with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

r_python = ''
for line in lines:
    r_python = line
    line.replace('Python', 'C++')

print(r_python)






