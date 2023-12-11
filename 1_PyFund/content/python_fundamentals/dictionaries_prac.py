dict_arr = {"name": "Josh", "age": 20, "email": "kjl@gmail.com"}

print(dict_arr)
dict_arr["name"] = "Lucido"
print(dict_arr)
del dict_arr["name"]
print(dict_arr)
dict_arr["first_name"] = "Kevin"
print(dict_arr)

print(len(dict_arr))
print(str(dict_arr))
print(type(dict_arr))

# add key:value pair
dict_arr["last_name"] = "Lucido"

# update key:value pairs
dict_arr.update({"first_name": "Kevin Joshua"})
dict_arr.update({"age": 25})
print(dict_arr)

x = dict_arr.get("age")
print(x)
