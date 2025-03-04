import pandas as pd
class Player:
    def __init__(self, name:str, position:str, age:int, team:str, stats:dict[str,float]):
        self.name = name
        self.position = position
        self.age = age
        self.team = team
        self.stats = stats  # Dictionary of player statistics (e.g., {'PPG': 25.3, 'APG': 7.2, 'RPG': 6.1})

    def __repr__(self):
        return 'Player({}, {}, {}, {},{})'.format(
                self.name,
                self.position,
                self.age,
                self.team,
                self.stats,
            )

read_data = pd.read_csv('NBA_stats.txt')
data_in_dictionary = read_data.to_dict(orient="records")# All the data converted to a dictionary
full_data = [] # Create an empty list to store all the data
for player_data in data_in_dictionary:
    Name = player_data["Player"]
    Position = player_data["Pos"]
    Age = player_data["Age"]
    Team = player_data["Tm"]
    # Extract relevant stats (columns 'TRB', 'AST', and 'PTS')
    Stats = {key: player_data[key] for key in player_data if key not in ["Player", "Pos", "Age","Tm"]}

    # Create Player object and add to list
    full_data.append(Player(Name, Position, Age, Team, Stats))