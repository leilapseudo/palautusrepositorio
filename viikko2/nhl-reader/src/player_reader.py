import requests
from player import Player


class PlayerReader:
    def __init__(self, url):
        self._url = url

    def get_players(self):
        response = requests.get(self._url, timeout=10)
        response.raise_for_status()
        player_data = response.json()

        return [Player(player) for player in player_data]
