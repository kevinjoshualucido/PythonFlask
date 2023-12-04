# x = [[5, 2, 3], [10, 8, 9]]
# students = [
#     {"first_name": "Michael", "last_name": "Jordan"},
#     {"first_name": "John", "last_name": "Rosales"},
# ]
# sports_directory = {
#     "basketball": ["Kobe", "Jordan", "James", "Curry"],
#     "soccer": ["Messi", "Ronaldo", "Rooney"],
# }
# z = [{"x": 10, "y": 20}]

# # 1.1
# print(x)
# x[1][0] = 15
# print(x)

# # 1.2
# print(students[0])
# students[0]["last_name"] = "Bryant"
# print(students[0])

# # 1.3
# print(sports_directory["soccer"])
# sports_directory["soccer"][0] = "Andres"
# print(sports_directory["soccer"])

# # 1.4
# print(z)
# z[0]["y"] = 30
# print(z)


students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]

# # 2
# def iterateDictionary(student_list):
#     for s in range(0, len(student_list)):
#         output = ""
#         for first_var, sec_var in student_list[s].items():
#             output += first_var + " - " + sec_var + " "
#         print(output)


# iterateDictionary(students)


# # 3
# def iterateDictionary(student_name, some_list):
#     for index in range(0, len(some_list)):
#         for key, val in some_list[index].items():
#             if key == student_name:
#                 print(val)


# iterateDictionary("last_name", students)


# 4
dojo = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": [
        "Michael",
        "Amy",
        "Eduardo",
        "Josh",
        "Graham",
        "Patrick",
        "Minh",
        "Devon",
    ],
}


def printInfo(some_dict):
    for key, val in some_dict.items():
        # print number of items in list along with key
        print(len(val), key.upper())
        # iterate through each value
        for each_val in range(0, len(val)):
            print(val[each_val])


printInfo(dojo)
