# filename = 'response.txt'
#
# ask_for_name = input("Hello, what is your name?")
# name = ask_for_name
#
#
# with open(filename, 'w') as file_object:
#     file_object.write(name)

filename = 'guest_book.txt'


while True:
    ask_for_name = input("Hello, what is your name?")
    name = ask_for_name
    break

with open(filename, 'w') as file_object:
    file_object.write(name)














