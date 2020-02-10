print("Please enter 'q' to quit the program.")

while True:

    try:

        number_1 = input("\nPlease enter a number: ")
        if number_1 == 'q':
            break
        number_1 = int(number_1)

        number_2 = input("Please enter a number: ")
        if number_2 == 'q':
            break
        number_2 = int(number_2)

    except ValueError:
        print("Please enter a number not a letter!!!")

    else:
        add_numbers = number_1 + number_2
        print(add_numbers)





