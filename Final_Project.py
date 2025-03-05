import pandas as pd
from numpy.ma.core import append


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

read_data = pd.read_csv('NBA_stats.csv')
data_in_dictionary = read_data.to_dict(orient="records") #all the data in a dictionary
full_data = []
for player_data in data_in_dictionary:
    Name = player_data["Player"]
    Position = player_data["Pos"]
    Age = player_data["Age"]
    Team = player_data["Tm"]
    # Extract relevant stats (columns 'TRB', 'AST', and 'PTS')
    Stats = {key: player_data[key] for key in player_data if key not in ["Player", "Pos", "Age","Tm"]}

    # Create Player object and add to list
    full_data.append(Player(Name, Position, Age, Team, Stats))


def search_for_player():
    inputs = input("Enter the player's full name in the order of First and Last name here:")
    for i in range(len(full_data)):
        if full_data[i].name.strip().lower() == inputs.strip().lower():
            print(full_data[i])

print(search_for_player())


def player_in_same_team(team_abbr:str)-> list[Player]:
    team_list = []
    for i in range(len(full_data)):
        if team_abbr == full_data[i].team:
            team_list.append(full_data[i])
    return team_list

# print(player_in_same_team("GSW"))


#def score_higher_than():