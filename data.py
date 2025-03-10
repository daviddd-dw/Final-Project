# Create a class of players that has attribute of
# the player's name, position, age, team and statistics.
# Author: David Wang and Nicolas Yenikomshian
class Player:
    def __init__(self, name:str, position:str, age:int, team:str, stats:dict[str,float]):
        self.name = name
        self.position = position
        self.age = age
        self.team = team
        self.stats = stats  # Dictionary of player statistics (e.g., {'PPG': 25.3, 'APG': 7.2, 'RPG': 6.1})

    def __repr__(self):
        return 'Name: {}\nPosition: {}\nAge: {}\nTeam: {}\nStats: {})'.format(
                self.name,
                self.position,
                self.age,
                self.team,
                self.stats,
            )