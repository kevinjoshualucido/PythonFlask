# while loops are another way of looping while a certain condition is true

# ex. with a for loop
for i in range(0, 5):
    print("for-loop = ", i)

# while loop
count = 0
while count < 5:
    print("while-loop = ", count)
    count += 1
# while loops express you to do something, including progress towards making the expression false

# practice with else and while loops
y = 5
while y <= 25:
    print("no. = ", y)
    y += 5
else:
    # if y > 25, end loop with statement
    print("End while-loop!")

# if our while loop is exited prematurely because of a break or return statement, then the else code section will never be executed.

for val in "string":
    if val == "i":
        break
    print(val)

word = "Lucido"
for i in word:
    if i == "d":
        break
    print(i)

another_word = "race"  # length = 9 BUT index = 8
# [0,1,2,3,4,5,6,7,8]   --> index value starts at 0!
# [J,o,v,a,n,o,v,i,c]

print(" ")

# prints word step by step
for i in range(0, len(another_word)):
    print(i + 1, another_word[i])
print(" ")

# prints word in reverse order
y = len(another_word) - 1
while y >= 0:
    print(y + 1, another_word[y])
    y -= 1
else:
    print(" ")

# BREAK terminates loop immediately and goes out of it
# CONTINUE skips whatever remaining statement and returns to the beginning of the loop

example_word = "love"
# [0,1,2,3]

for value in example_word:
    if value == "v":
        continue
    print(value)
# output: l,o,e

y = len(example_word) - 1
while y >= 0:
    if example_word[y] == "o":
        y -= 1
        continue
    print(example_word[y])
    y -= 1
# output: e,v,l