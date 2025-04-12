# Manages probability-related calculations

# filepath: c:\Users\Nicol\Desktop\Software\Generala\controllers\probability_controller.py
from models.probability import calculate_all_probabilities

class ProbabilityController:
    """Controller for handling probability calculations in the Generala game."""
    
        
    def calculate_probabilities(self, dice_values, rolls_remaining):
        """
        Calculate probabilities for all combinations based on dice values and rolls remaining.
        
        :param dice_values: List of current dice values
        :param rolls_remaining: Number of rolls remaining
        :return: Dictionary of probabilities or None if calculation not possible
        """
        # Only calculate if we have rolls remaining and valid values
        if rolls_remaining > 0 and None not in dice_values:
            return calculate_all_probabilities(dice_values, rolls_remaining)
        return None
        
    def get_best_combination(self, dice_values, rolls_remaining):
        """
        Get the combination with the highest probability.
        
        :param dice_values: List of current dice values
        :param rolls_remaining: Number of rolls remaining  
        :return: Tuple of (combination, probability) or None
        """
        probabilities = self.calculate_probabilities(dice_values, rolls_remaining)
        if not probabilities:
            return None
            
        return max(probabilities.items(), key=lambda x: x[1])