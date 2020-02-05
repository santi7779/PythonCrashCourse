# prompt = "\nWhat kind of pizza toppings would you like? "
# prompt += "\nEnter 'quit' to end the program "
#
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(f"I'll add {message} to your pizza")

# prompt = "\nHow old are you? "
#
# message = ""
#
# while True:
#     message = input(prompt)
#     message = int(message)
#
#     if message < 3:
#         print("Your movie ticket is free!!!")
#     elif message < 12:
#         print("Your movie ticket is $10!!!")
#     else:
#         print("Your movie ticket is $15!!!")
#     break

prompt = "\nHow old are you? "
prompt += "\nEnter 'quit' to end the program "

message = ""

while message != 'quit':
    message = input(prompt)
    message = int(message)

    if message < 3:
        print("Your movie ticket is free!!!")
    elif message < 12:
        print("Your movie ticket is $10!!!")
    else:
        print("Your movie ticket is $15!!!")












