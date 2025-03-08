# Author: David Wang

import unittest
import driver
import player

class TestCases(unittest.TestCase):
    def test_search_for_player_1(self):
        inputs = "stephen curry"
        expected = player.full_data[102]
        self.assertEqual(expected, driver.search_for_player(inputs))

    def test_search_for_player_2(self):
        inputs = "curry 30"
        expected = "No player is found"
        self.assertEqual(expected, driver.search_for_player(inputs))

    def test_player_in_same_team_1(self):
        inputs = "bos"
        expected = ['Dalano Banton', 'Oshae Brissett', 'Jaylen Brown',
                    'JD Davison', 'Sam Hauser', 'Jrue Holiday',
                    'Al Horford', 'Luke Kornet', 'Svi Mykhailiuk',
                    'Drew Peterson', 'Kristaps Porziņģis', 'Payton Pritchard',
                    'Neemias Queta', 'Lamar Stevens', 'Jayson Tatum', 'Derrick White']
        self.assertEqual(expected, driver.player_in_same_team(inputs))

    def test_player_in_same_team_2(self):
        inputs = "35"
        expected = ["Input should be letters"]
        self.assertEqual(expected, driver.player_in_same_team(inputs))

    def test_score_higher_than_1(self):
        inputs = "30"
        expected = ['Giannis Antetokounmpo', 30.9, 'Luka Dončić', 33.4,
                    'Joel Embiid', 35.0, 'Shai Gilgeous-Alexander', 31.2]
        self.assertEqual(expected, driver.score_higher_than(inputs))

    def test_score_higher_than_2(self):
        inputs = "40"
        expected = []
        self.assertEqual(expected, driver.score_higher_than(inputs))