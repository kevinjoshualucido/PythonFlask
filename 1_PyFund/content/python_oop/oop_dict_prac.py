class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

# player_kd = Player("Kevin Durant", 35, "SF", "Phoenix Suns")
# print(player_kd.name)


kevin = {"name": "Kevin Durant", "age": 34, "position": "SF", "team": "Phoenix Suns"}
print(kevin["name"])

player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
print(player_kevin.name)