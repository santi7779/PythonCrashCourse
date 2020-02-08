class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name}.")
        print(f"The cuisine of this restaurant is {self.cuisine_type}.")

    def open_restaurant(self):
        print("The restaurant is open.")


restaurant = Restaurant('Bolis', 'Pizzas')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("")
restaurant1 = Restaurant('Outback Steakhouse', 'Aussie Onions')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
print("")
restaurant2 = Restaurant('Franks', 'Fish and Chips')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

class User:

    def __init__(self, first_name, last_name, hair_color, height):
        self.first_name = first_name
        self.last_name = last_name
        self.hair_color = hair_color
        self.height = height

    def describe_user(self):
        print(f"The user's first name is {self.first_name}.")
        print(f"The user's last name is {self.last_name}.")
        print(f"The user's hair color is {self.hair_color}.")
        print(f"The user's is {self.height} tall.")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!!!")

user1 = User('Billy', 'Blanks', 'Brown', '172cm')
user1.describe_user()
user1.greet_user()
print("")
user2 = User('Fred', 'Smith', 'Green', '165cm')
user2.describe_user()
user2.greet_user()
print("")
user3 = User('Tom', 'Jones', 'Red', '180cm')
user3.describe_user()
user3.greet_user()





