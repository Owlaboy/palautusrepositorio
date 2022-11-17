from playerreader import PlayerReader

class PlayerStats():
    def __init__(self, response):
        self.response = response

    def top_scores_by_nationality(self, countrycode):
        players = []
        for player_dict in self.response:
            if player_dict.nationality == countrycode:
                players.append(player_dict)
        players.sort(key=lambda player: player.goals + player.assists, reverse=True)
        return players