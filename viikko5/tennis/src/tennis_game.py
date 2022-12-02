class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        if player_name == "player2":
            self.player2_score += 1

    def get_score(self):
        score = ""
        second_lastpoint = 3
        last_point = 4


        if self.player1_score == self.player2_score:
            equal_score_strings = ["Love-All", "Fifteen-All", "Thirty-All", "Forty-All", "Deuce"]
            if self.player1_score > second_lastpoint:
                score = equal_score_strings[4]
            else:
                score = equal_score_strings[self.player1_score]

        elif self.player1_score >= last_point or self.player2_score >= last_point:
            point_difference = self.player1_score - self. player2_score
            advantage_point_difference_player1 = 1
            advantage_point_difference_player2 = -1
            victory_point_difference_player1 = 2
            victory_point_difference_player2 = -2

            if point_difference == advantage_point_difference_player1:
                score = "Advantage player1"
            elif point_difference == advantage_point_difference_player2:
                score = "Advantage player2"
            elif point_difference >= victory_point_difference_player1:
                score = "Win for player1"
            elif point_difference <= victory_point_difference_player2:
                score = "Win for player2"

        else:
            score_strings = ["Love", "Fifteen", "Thirty", "Forty"]
            score = f"{score_strings[self.player1_score]}-{score_strings[self.player2_score]}"

        return score
