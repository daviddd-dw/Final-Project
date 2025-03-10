# Author: David Wang

import pandas as pd
import data

read_data = pd.read_csv('NBA_stats.txt') # read data from the text file
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
    full_data.append(data.Player(Name, Position, Age, Team, Stats))
