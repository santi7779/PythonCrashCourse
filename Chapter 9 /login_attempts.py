class User:

    def __init__(self, first_name, last_name, hair_color, height):
        self.first_name = first_name
        self.last_name = last_name
        self.hair_color = hair_color
        self.height = height
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user's first name is {self.first_name}.")
        print(f"The user's last name is {self.last_name}.")
        print(f"The user's hair color is {self.hair_color}.")
        print(f"The user's is {self.height} tall.")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!!!")

    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('Billy', 'Blanks', 'Brown', '172cm')
user1.describe_user()
user1.greet_user()

print("\nMaking nine login attempts.")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"login attempts: {user1.login_attempts}")
print(f"\nResetting Login Attempts.")
user1.reset_login_attempts()
print(f"The login attempts counter has been reset to {user1.login_attempts}")




