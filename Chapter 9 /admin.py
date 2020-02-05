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


class Admin(User):

    def __init__(self, first_name, last_name, hair_color, height):
        super().__init__(first_name, last_name, hair_color, height)
        self.privileges = Privileges()


class Privileges:

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("The Admin user has the following privileges: ")
        for privilege in self.privileges:
            print(f"- {privilege.title()}")


admin1 = Admin('Billy', 'Blanks', 'Brown', '172cm')
admin1.privileges = ["can add post", "can delete post", "can ban user"]


admin1.privileges.privileges = admin1_privileges
admin1.privileges.show_privileges()

