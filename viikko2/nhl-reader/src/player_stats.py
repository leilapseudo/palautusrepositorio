"""Provides statistics for NHL players."""


class PlayerStats:
    """Calculates statistics for NHL players."""

    def __init__(self, reader):
        """Initialize statistics using a player reader."""
        self._players = reader.get_players()

    def top_scorers_by_team(self, team_name):
        """Return players from a team sorted by total points."""
        players_of_team = [
            player for player in self._players
            if player.team == team_name
        ]

        return sorted(
            players_of_team,
            key=lambda player: player.goals + player.assists,
            reverse=True
        )

    def top_scorers_by_nationality(self, nationality):
        """Return players of a nationality sorted by total points."""
        players = [
            player for player in self._players
            if player.nationality == nationality
        ]

        return sorted(
            players,
            key=lambda player: player.goals + player.assists,
            reverse=True
        )
        