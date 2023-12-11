class User:
    # create construcor and its instance attributes
    def __init__(self, name, email):
        self.name = name
        self.email = email
    # create the instance method 'greeting'
    def greeting(self):
        print(f"Hello there, {self.name}!")

user1 = User("Josh", "josh#email.com")
user1.greeting()

user2 = User("Sarah", "sarah@email.com")
user2.greeting()