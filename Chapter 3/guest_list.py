guest_list = ["Billy Blanks", "Fred Hoopy", "Trevor Nobu"]

print(f"Hello, {guest_list[0]} would you like to come to dinner?")
print(f"Hello, {guest_list[1]} would you like to come to dinner?")
print(f"Hello, {guest_list[2]} would you like to come to dinner?")

print(f"\nOh no, {guest_list[1]} can't make it tonight!!!")

del guest_list[1]
guest_list.insert(1, "Jamie MagicTorch")

print(f"\nHello, {guest_list[0]} would you like to come to dinner?")
print(f"Hello, {guest_list[1]} would you like to come to dinner?")
print(f"Hello, {guest_list[2]} would you like to come to dinner?")

print("\nI've found a bigger dinner table!!!")

guest_list.insert(0, "Fred Williams")
guest_list.insert(2, "Scot Walker")
guest_list.append("Trevor Gates")

print(f"\nHello, {guest_list[0]} would you like to come to dinner?")
print(f"Hello, {guest_list[1]} would you like to come to dinner?")
print(f"Hello, {guest_list[2]} would you like to come to dinner?")
print(f"Hello, {guest_list[3]} would you like to come to dinner?")
print(f"Hello, {guest_list[4]} would you like to come to dinner?")
print(f"Hello, {guest_list[5]} would you like to come to dinner?")

print("\nI can only invite two people to dinnner!!!")

popped_guest = guest_list.pop()
print(f"\nSorry {popped_guest} you can't come to dinner!!!")
popped_guest = guest_list.pop()
print(f"Sorry {popped_guest} you can't come to dinner!!!")
popped_guest = guest_list.pop()
print(f"Sorry {popped_guest} you can't come to dinner!!!")
popped_guest = guest_list.pop()
print(f"Sorry {popped_guest} you can't come to dinner!!!")

print(f"\nHello, {guest_list[0]} you can still come to dinner!!!")
print(f"Hello, {guest_list[1]} you can still come to dinner!!!")
print("")
number_of_guests = len(guest_list)
print(f"I'm inviting {number_of_guests} guests to dinner")

del guest_list[0:2]
print("")
print(guest_list)

