word = "hello"
for i in word:
    print(i)


# break
print(" ")


for i in "there":
    print(i)


# break
print(" ")


list_arr = ["xyz", 123, "abc", 456]
tupl_arr = ("Kevin", "Lucido", 25, 175)
dict_arr = {"first_name": "Kevin", "last_name": "Lucido", "age": 25, "height": 175}

# practicing loops with a list
for j in list_arr:
    print(j)

# practicing loops with a tuple
for j in tupl_arr:
    print(j)

# practicing loops with a dictionary
for j in dict_arr:
    # logging only the index will get the key
    # logging the dictionary with the loop variable 'j' (which becomes the index of the dictionary itself) gives us the value of each key
    print(dict_arr[j])


# break
print(" ")


# grab the index position and its value
abc_arr = ["a", "b", "c", "d", "e", "f", "g"]
for i in range(0, len(abc_arr)):
    print(i + 1, abc_arr[i])

names_arr = ["Kevin", "Sarah", "Liam", "Julian", "Kayden"]
for x in range(0, len(names_arr)):
    print((x + 1), names_arr[x])
