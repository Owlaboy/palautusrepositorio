import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 0)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.stats = Statistics(PlayerReaderStub())
    
    def test_search_returns_none_if_player_is_not_found(self):
        self.assertIsNone(self.stats.search("Koivu"))
    
    def test_search_returns_player_if_player_is_found(self):
        self.assertEqual(self.stats.search("Kurri").name, "Kurri")
    
    def test_team_returns_correct_list(self):
        self.assertEqual(len(self.stats.team("EDM")), 2)


    def test_top_returns_correct_list_points(self):
        sortedList = self.stats.top(3, 1)
        self.assertEqual(sortedList[0].name, "Lemieux")
        self.assertEqual(sortedList[1].name, "Kurri")
        self.assertEqual(sortedList[2].name, "Yzerman")

    def test_top_returns_correct_list_goals(self):
        sortedList = self.stats.top(3, 2)
        self.assertEqual(sortedList[0].name, "Lemieux")
        self.assertEqual(sortedList[1].name, "Yzerman")
        self.assertEqual(sortedList[2].name, "Kurri")
    
    def test_top_returns_correct_list_assists(self):
        sortedList = self.stats.top(3, 3)
        self.assertEqual(sortedList[0].name, "Lemieux")
        self.assertEqual(sortedList[1].name, "Kurri")
        self.assertEqual(sortedList[2].name, "Semenko")
    
    