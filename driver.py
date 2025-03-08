import data
import player
full_data = player.full_data

# based on the user input, this function prints a single player's statistics
# user type strings as inputs
# The function returns print strings in the console
# Author: Nick and David
def search_for_player(player_name:str)-> data.Player:
    the_player = ""
    for i in range(len(full_data)):
        if full_data[i].name.strip().lower() == player_name.strip().lower():
            the_player = full_data[i]
            print(i)
            break
        else:
            the_player = "No player is found"
    return the_player

input1 = input("Enter the player's full name in the order of First and Last name here:")
print(search_for_player(input1))

# This function sorts a list of players who are in the same team
# team_abbr:str is a string of a team's abbreviation
# The function returns all the players name in that team
# Author: David Wang
def player_in_same_team(team_abbr:str)-> list:
    name_list = []
    if not team_abbr.isalpha():
        return ["Input should be letters"]
    for i in range(len(full_data)):
        if team_abbr.lower() == full_data[i].team.lower():
            name_list.append(full_data[i].name)
    if not name_list:
        return ["Team not found"]
    return name_list

input2 = input("Enter the team's abbreviation here to see the players in that team:")
print(player_in_same_team(input2))

# This function finds a list of player's statistics
# user type strings as inputs
# The function returns a list of player's statistics who score higher than the input number
# Returns ValueError if the input is not a number
# Author: Nick and David
def score_higher_than(inputs:str) -> print:
    score_list = []
    try:
        for i in range(len(full_data)):
            if int(inputs) < full_data[i].stats["PTS"]:
                score_list.append(full_data[i].name)
                score_list.append(full_data[i].stats["PTS"])
        return score_list
    except ValueError as e:
        return print("The input should be a number, got", e)

input3 = input("Type a number here to check players who score more than that:")
print(score_higher_than(input3))