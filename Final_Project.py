import pandas as pd

class NBA_player:
    def __init__(self,name,score,age):
        self.name = name
        self.score = score
        self.age = age



df = pd.read_csv('NBA_2024_per_game(03-01-2024).csv')

filtered_df = df[df['PTS'] > 30]
print(filtered_df)
