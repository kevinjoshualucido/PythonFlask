print("Assignment 1")
print("================")

# content here

# 1
print("---1. Basic---")
for int in range(0, 151):
    print(int)

# 2
print("---2. Multiples of five---")
for int in range(5, 1_001, 5):
    print(int)

# 3
print("---3. Counting, the Dojo Way---")
for x in range(1, 101):
    if (x % 10) == 0:
        print("Coding Dojo")
    elif (x % 5) == 0:
        print("Coding")
    else:
        print(x)

# 4
print("---4. Whoa. That sucker's huge---")
final_sum = 0
for adding_sums in range(0, 500_001):
    if not (adding_sums % 2) == 0:
        final_sum += adding_sums
print(final_sum)

# 5
print("---5. Countdown by fours---")
six_years_ago = 2018
while six_years_ago >= 0:
    print(six_years_ago)
    six_years_ago -= 4

# 6
print("---6. Flexible counters---")
low_num = 3
high_num = 27
multiple = 3
if multiple > high_num or multiple < low_num:
    print("not applicable")
for i in range(low_num, high_num + 1):
    if (i % multiple) == 0:
        print(i)

print("================")
# end
