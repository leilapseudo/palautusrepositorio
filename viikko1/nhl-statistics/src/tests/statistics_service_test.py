import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_player(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_does_not_find_player(self):
        player = self.stats.search("Selanne")
        self.assertIsNone(player)

    def test_team_returns_players_from_team(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)

    def test_team_returns_empty_list_if_no_players(self):
        players = self.stats.team("NYR")
        self.assertEqual(len(players), 0)

    def test_top_returns_players_in_points_order(self):
        players = self.stats.top(2)
        self.assertEqual(len(players), 2)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")

    def test_top_sorts_by_points(self):
        players = self.stats.top(2, SortBy.POINTS)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")

    def test_top_sorts_by_goals(self):
        players = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(players[0].name, "Lemieux")
        self.assertEqual(players[1].name, "Yzerman")

    def test_top_sorts_by_assists(self):
        players = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Yzerman")
