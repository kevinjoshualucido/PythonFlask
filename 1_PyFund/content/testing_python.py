import random

print("Welcome to Python!")

print("This is a loop printing 5x")
for i in range(1, 6):
    print(f"x is: {i}")

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
day = random.choice(weekdays)
print(f"Today is: {day}")

if day == "Monday":
    print("It'll be a long week :/")
elif day == "Friday":
    print("It's Friday theeen it's Saturday! Sunday! What!?")
else:
    print("Not quite there yet...")
