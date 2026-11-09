"""Defines the Player class."""
class Player:
    """Represents an NHL player."""""
    def __init__(self, player):
        self.name = player["name"]
        self.nationality = player["nationality"]
        self.team = player["team"]
        self.goals = player["goals"]
        self.assists = player["assists"]

    def __str__(self):
        return (
            f"{self.name} team {self.team} "
            f"goals {self.goals} assists {self.assists}"
        )
