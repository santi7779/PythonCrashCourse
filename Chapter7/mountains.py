# sandwich_orders = ["ham", "beef", "budster", "old smokey", "steak and cheese"]
# finished_sandwiches = []
#
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#
#     print(f"I made your {current_sandwich} sandwich!!!")
#     finished_sandwiches.append(current_sandwich)
#
# for finished_sandwich in finished_sandwiches:
#     print(f"The {finished_sandwich} sandwich has been made.")

# sandwich_orders = ["ham", "beef", "pastrami", "pastrami", "steak and cheese", "pastrami", "mango chutney"]
# finished_sandwiches = []
# print("The deli has run out of pastrami!!!")
#
# while "pastrami" in sandwich_orders:
#     sandwich_orders.remove("pastrami")
#
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#
#     print(f"I made your {current_sandwich} sandwich!!!")
#     finished_sandwiches.append(current_sandwich)
#
# for finished_sandwich in finished_sandwiches:
#     print(f"The {finished_sandwich} sandwich has been made.")

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let someone else respond? yes/no ")
    if repeat == "no":
        polling_active = False

print("\n---Poll Results---")

for name, response in responses.items():
    print(f"{name} would like to visit {response}!!!")








































