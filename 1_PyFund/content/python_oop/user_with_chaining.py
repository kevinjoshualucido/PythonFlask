class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False  # default to nonrewards member
        self.rewards_points = 0  # nonrewards member has with no points

    # method prints all user data on separate lines
    def display_info(self):
        print(f"{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n")
        return self

    # method enrolls user into the rewards program
    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member!")
            return self
        else:
            self.is_rewards_member = True
            self.rewards_points += 200
            print(
                f"Thank you for signing up to be a rewards member!\nYou have {self.rewards_points} rewards points"
            )
        return self

    # method subtracts user's points by amount specified
    def spend_points(self, amount):
        if not self.is_rewards_member == True:
            print(
                "You are not enrolled as a member! Please enroll now to spend rewards points!"
            )
            return self
        if not amount > 0:
            print("Invalid input!")
            return self
        if self.rewards_points < amount:
            print("You do not have enough points to spend!")
            return self
        else:
            self.rewards_points -= amount
            print(
                f"You've spent {amount} point(s)\nYour total is now {self.rewards_points} rewards points"
            )
            return self


user1 = User("Kevin", "Leyva", "kevinlucido@gmail.com", 25)
user2 = User("Josh", "Lucido", "joshgonzalez@gmail.com", 22)
user3 = User("Sarah", "Mledenovic", "sarahmledenovic@gmail.com", 27)

# chaining
user1.display_info().enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()
