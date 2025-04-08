# Dice representation and rolling

import random

class Die: 
    """Represents a single die with configurable number of sides."""
    def __init__(self, faces=6):
        """Initialize a die with a given number of faces (6 by default)."""
        self.faces = faces
        self.value = None

    def roll(self):
        """Roll the die and return the result."""
        self.value = random.randint(1, self.faces)
        return self.value
    
class DiceSet:
    """represents a set of dice used in Generala"""

    def __init__(self, dice_count=5, faces=6):
        """
        Initialize a set of dice with a given count (default: 5) and faces (default: 6).
        """
        self.dice = [Die(faces) for _ in range(dice_count)]
        self.throw_count = 0  # Initialize throw count
        self.max_throws = 3
        
    def reset_throw_count(self):
        """Reset the throw count to 0"""
        self.throw_count = 0
        return self.throw_count

    def roll_all(self):
        """
        Roll all dice in the set and return their values.
        """
        if self.throw_count < self.max_throws:
            self.throw_count += 1
            values = [die.roll() for die in self.dice]
            return self.throw_count, values
        return self.throw_count, self.get_values()
        
    
    def roll_selected(self, indices):
        """
        Roll only the selected dice in the set and return their values.
        """
        if self.throw_count < self.max_throws:
            self.throw_count += 1
            for index in indices:
                if 0 <= index < len(self.dice):
                    self.dice[index].roll()
            return self.throw_count, self.get_values()
        return self.throw_count, self.get_values()
        
    def get_values(self):
        """
        Get the current values of all dice in the set.
        """
        return [die.value for die in self.dice]
    
    def get_throw_state(self):
        """Get the current throwing state (throw number and dice values)."""
        return self.throw_count, self.get_values()
    
    def __str__(self):
        """String representation of the dice set."""
        return f"Throw #{self.throw_count}: Dice values: {self.get_values()}"

