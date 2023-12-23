class Player:
    def __init__(self, key):
        self.name = key["name"]
        self.age = key["age"]
        self.position = key["position"]
        self.team = key["team"]

    def __repr__(self):
        display = f"Player: {self.name}, {self.age} yo,\nPos: {self.position}, Team: {self.team}"
        return display

    @classmethod
    def add_players(cls, data):
        player_objects = []
        for dict in data:
            player_objects.append(cls(dict))
        return player_objects


players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics",
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers",
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers",
    },
    {"name": "", "age": 16, "position": "P", "team": "en"},
]


kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets",
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics",
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets",
}

player_kd = Player(kevin)
player_jt = Player(jason)
player_ki = Player(kyrie)
print(player_kd)
print(player_jt)
print(player_ki)


new_team = []
for player_dict in players:
    player = Player(player_dict)
    new_team.append(player)

print(new_team)
