"""Reads NHL player data from an API."""
import requests
from player import Player

class PlayerReader:
    """Fetches and parses player data."""

    def __init__(self, url):
        """Initialize the reader with an API URL."""
        self._url = url

    def get_players(self):
        """Fetch players from the API."""
        response = requests.get(self._url, timeout=10)
        response.raise_for_status()
        player_data = response.json()

        return [Player(player) for player in player_data]
