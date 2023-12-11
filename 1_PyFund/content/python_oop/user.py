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


# instantiate user1
user1 = User("Kevin", "Leyva", "kevinlucido@gmail.com", 25)

# enroll user1 into rewards program and print status and points to the console
user1.enroll()
print("Is rewards member: ", user1.is_rewards_member)
print("Sign up points: ", user1.rewards_points)

# make 2 more instances of the user class
user2 = User("Josh", "Lucido", "joshgonzalez@gmail.com", 22)
user3 = User("Sarah", "Mledenovic", "sarahmledenovic@gmail.com", 27)

# user1 spends 50 points
user1.spend_points(50)

# user 2 enrolls
user2.enroll()

# user2 spends 80 points
user2.spend_points(80)

# print user info in the console
print(user1.display_info())
print(user2.display_info())
print(user3.display_info())

# # test to see if the if-statement for enroll() is working
# user should get message that they are already enrolled
# user1.enroll()

# test to see if the if-statment for spend_points() is working
# user1 only has 150 points left so not enough points to spend
user1.spend_points(200)
# user3 is not a member but tries to spend 40 points
user3.spend_points(40)
