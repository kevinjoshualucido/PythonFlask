# contact_card = {
#     "first_name": "Kevin Joshua",
#     "last_name": "Lucido",
#     "age": 25,
#     "dob": "1998.05.01",
# }


# for each_key in contact_card:
#     print(contact_card[each_key])


capitals = {
    "Washington": "Olympia",
    "California": "Sacramento",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Texas": "Austin",
    "Oklahoma": "Oklahoma City",
    "Virginia": "Richmond",
}
# another way to iterate through the keys
for each_key in capitals.keys():
    print(each_key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
# to iterate through the values
for each_val in capitals.values():
    print(each_val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc