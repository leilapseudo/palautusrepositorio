"""Tests for PlayerStats."""

import unittest

from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    """A stub for reading test players."""

    def get_players(self):
        """Return a predefined list of players."""
        return [
            Player({
                "name": "Semenko",
                "nationality": "CAN",
                "team": "EDM",
                "goals": 4,
                "assists": 12
            }),
            Player({
                "name": "Lemieux",
                "nationality": "CAN",
                "team": "PIT",
                "goals": 45,
                "assists": 54
            }),
            Player({
                "name": "Kurri",
                "nationality": "FIN",
                "team": "EDM",
                "goals": 37,
                "assists": 53
            }),
            Player({
                "name": "Yzerman",
                "nationality": "USA",
                "team": "DET",
                "goals": 42,
                "assists": 56
            }),
            Player({
                "name": "Gretzky",
                "nationality": "CAN",
                "team": "EDM",
                "goals": 35,
                "assists": 89
            }),
        ]


class TestPlayerStats(unittest.TestCase):
    """Tests for the PlayerStats class."""

    def setUp(self):
        """Initialize PlayerStats with a stub reader."""
        self.stats = PlayerStats(PlayerReaderStub())

    def test_team_returns_players_from_team(self):
        """Test that only players from the selected team are returned."""
        players = self.stats.top_scorers_by_team("EDM")
        self.assertEqual(len(players), 3)

    def test_team_sorts_players_by_points_descending(self):
        """Test that players are sorted by points in descending order."""
        players = self.stats.top_scorers_by_team("EDM")
        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Kurri", "Semenko"]
        )

    def test_team_returns_empty_list_if_no_players(self):
        """Test that an unknown team returns an empty list."""
        players = self.stats.top_scorers_by_team("NYR")
        self.assertEqual(players, [])
        