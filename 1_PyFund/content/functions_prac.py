def add(a, b):
    x = a + b
    return x


sum1 = add(4, 6)
sum2 = add(1, 4)
sum3 = sum1 + sum2
print(sum3)


def full_name(first_name, last_name):
    return first_name + " " + last_name


name1 = full_name("Eddie", "Aikau")
print(name1)
name2 = full_name("Kevin", "Lucido")
print(name2)


def gm(name="Josh", repeat=2):
    print(f"Hello there {name}\n" * repeat)


gm()
gm("Kevin")
gm("Sarah", 3)
# argument order doesn't matter as long as we are expicit with our parameters
gm(repeat=4, name="Louise")