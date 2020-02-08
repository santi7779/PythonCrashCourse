class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 10

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name}.")
        print(f"The cuisine of this restaurant is {self.cuisine_type}.")

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self, number):
        self.number_served = number
        print(f"The restaurant has served {number} people.")

    def increment_number_served(self, number):
        self.number_served += number
        print(f"The restaurant has served {number} people.")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type="ice cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


mr_whipple = IceCreamStand('Bolis')
mr_whipple.flavors = ["vanilla", "strawberry", "chocolate"]
mr_whipple.describe_restaurant()
mr_whipple.open_restaurant()
mr_whipple.display_flavors()


