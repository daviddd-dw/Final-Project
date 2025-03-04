import data

full_data = data.full_data

# based on the user input, this function prints a single player's statistics
# user type strings as inputs
# The function returns print strings in the console
def search_for_player()-> print:
    inputs = input("Enter the player's full name in the order of First and Last name here:")
    for i in range(len(full_data)):
        if full_data[i].name.strip().lower() == inputs.strip().lower():
            return print(full_data[i])

# This function sorts a list of players who are in the same team
# team_abbr:str is a string of a team's abbreviation
# The function returns all the players name in that team
def player_in_same_team(team_abbr:str)-> list[data.Player]:
    name_list = []
    for i in range(len(full_data)):
        if team_abbr == full_data[i].team:
            name_list.append(full_data[i].name)
    return name_list

print(player_in_same_team("BOS"))

# This function finds a list of player's statistics
# user type strings as inputs
# The function returns a list of player's statistics who score higher than the input number
def score_higher_than() -> print:
    inputs = input("Type a number here to check players who score more than that:")
    score_list = []
    try:
        for i in range(len(full_data)):
            if int(inputs) < full_data[i].stats["PTS"]:
                score_list.append(full_data[i])
        return print(score_list)
    except ValueError as e:
        return print("The input should be a number, got", e)


score_higher_than()