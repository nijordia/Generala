# Controls game flow
from models.dice import DiceSet
from models.game_state import Scoreboard
from models.probability import calculate_all_probabilities
from models.score import calculate_score

class GameController:
    """
    Controls the flow of a Generala game.
    """
    def __init__(self, player_names):
        """
        Initialized a new game with the specigied players.
        :param plater_names: A list of strings representing plater names"""

        if not player_names or len(player_names) < 1:
            raise ValueError("At least two player names are required.")
        
        self.players = player_names
        self.scoreboards = {player: Scoreboard() for player in player_names}
        self.dice_set = DiceSet()
        self.current_player_idx = 0
        self.current_round = 1
        self.max_rounds = 11 # 11 combinations to play

    def get_current_player(self):
        """
        Returns the name of the current player as a string.
        """
        return self.players[self.current_player_idx]
    
    def roll_dice(self, indices=None):
        """
        Roll the dice - either all or selected indices.
        :param indices: Optional list of dice indices to roll. If None, roll all dice.
        :return: Tuple of (throw_count, dice_values)
        """

        if indices is None:
            return self.dice_set.roll_all()
        else:
            return self.dice_set.roll_selected(indices)

    def calculate_probabilities(self):
        """
        Calculate the probabilities of achieving different combinations with the
        current dice. :return: Dictionary of probabilities for each combination.
        """
        dice_values = self.dice_set.get_values()
        rolls_remaining = self.dice_set.max_throws - self.dice_set.throw_count

        if None in dice_values or rolls_remaining < 1:
            return {}
        
        return calculate_all_probabilities(dice_values, rolls_remaining)
    
    def score_combination(self, combination):
        """
        Score the current combination for the current player.
        :param combination: The combination to score.
        :return: The score for the combination.
        """
        player = self.get_current_player()
        dice_values = self.dice_set.get_values()
        rolls_remaining = self.dice_set.max_throws - self.dice_set.throw_count

        # Calculate Score
        score = calculate_score(combination, dice_values, rolls_remaining)

        # Record score in player's scoreboard
        self.scoreboards[player].add_score(combination, score)
        
        return score
    
    def cross_out_combination(self, combination):
        """
        Cross out a combination (score 0) for the current player.
        :param combination: The combination to cross out.
        """
        player = self.get_current_player()
        self.scoreboards[player].cross_out(combination)

    def next_turn(self):
        """
        End the current player's turn and move to the next player.
        If all players have played, advanced to the next round. 
        :return: True if the fame continues, False if the game is over.
        """
        # Reset dice for next player
        self.dice_set.reset_throw_count()

        # If we've completed a full round of players
        if self.current_player_idx == 0: # How does this variable work?
            self.current_round += 1
        
        # Check if game is over
        if self.current_round > self.max_rounds:
            return False
        
        return True
    
    def get_available_combinations(self):
        """
        Get the available combinations for the current player.
        :return: List of available combinations. 
        """
        player = self.get_current_player()
        return self.scoreboards[player].get_available_combinations()

    def get_scores(self):
        """
        Get the scores for all platers.
        :return: Dictionary mapping player names to their scores.
        """
        return {player: self.scoreboards[player].get_total_score() for player in self.players}
    
    def get_winner(self):
        """"
        Determine the winner of the game. 
        :return: The name of the player with the highest score.
        """
        scores = self.get_scores()
        max_score = max(scores.values())
        winners = [player for player, score in scores.items() if score == max_score]
        return winners
    
































