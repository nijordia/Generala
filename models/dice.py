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
        """Initialize a set of dice with a given count (default: 5) and faces (default: 6)."""
        self.dice = [Die(faces) for _ in range(dice_count)]

    def roll_all(self):
        """Roll all dice in the set and return their values."""
        return [die.roll() for die in self.dice]
    
    def roll_selected(self, indices):
        """Roll only the selected dice in the set and return their values."""
        for index in indices:
            if 0 <= index < len(self.dice):
                self.dice[index].roll()
        return [die.value for die in self.dice]
    
    def get_values(self):
        """Get the current values of all dice in the set."""
        return [die.value for die in self.dice]
    
    def __str__(self):
        """String representation of the dice set."""
        return f"Dice values: {self.get_values()}"


