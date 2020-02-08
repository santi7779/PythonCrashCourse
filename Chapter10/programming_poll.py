filename = 'poll.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name? ")
    question = input("Why do you like programming?")
    if name == 'quit':
        break
    if question == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{name} {question} \n")
        print(f"Hi {name}, thank you for your response.")


