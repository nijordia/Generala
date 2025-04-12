

# Run test using this command from the root: python -m test.test_models_probability

from models.dice import DiceSet
from models.probability import (
    calculate_generala_probability,
    calculate_poker_probability,
    calculate_full_probability,
    calculate_escalera_probability,
    calculate_all_probabilities
)

def test_integration_with_dice():
    """Test that the probability functions work well with our DiceSet class"""
    print("==== Testing Probability Integration with DiceSet ====")
    
    # Create a dice set and roll it
    dice_set = DiceSet()
    throw_num, dice_values = dice_set.roll_all()
    
    # Calculate remaining rolls
    rolls_remaining = dice_set.max_throws - throw_num
    
    print(f"Dice rolled: {dice_values} (throw #{throw_num}, {rolls_remaining} rolls remaining)")
    
    # Calculate probabilities based on current dice state
    probabilities = calculate_all_probabilities(dice_values, rolls_remaining)
    
    print("\nProbabilities for each combination:")
    for combination, probability in probabilities.items():
        print(f"- {combination}: {probability:.2%}")

    # Roll again (selectively) and recalculate
    print("\n==== Rolling Selected Dice ====")
    indices_to_reroll = [0, 2, 4]  # Reroll first, third, and fifth dice
    throw_num, dice_values = dice_set.roll_selected(indices_to_reroll)
    rolls_remaining = dice_set.max_throws - throw_num
    
    print(f"After rerolling indices {indices_to_reroll}: {dice_values} (throw #{throw_num}, {rolls_remaining} rolls remaining)")
    
    # Calculate new probabilities
    probabilities = calculate_all_probabilities(dice_values, rolls_remaining)
    
    print("\nUpdated probabilities for each combination:")
    for combination, probability in probabilities.items():
        print(f"- {combination}: {probability:.2%}")

def test_specific_dice_configurations():
    """Test probability calculations with specific dice configurations"""
    print("\n==== Testing Specific Dice Configurations ====")
    
    # Test case 1: Almost Generala (4 of a kind)
    dice_values = [6, 6, 6, 6, 2]
    print(f"\nTest case 1 - Almost Generala: {dice_values}")
    
    # Test with 1 roll remaining
    probabilities = calculate_all_probabilities(dice_values, 1)
    print("With 1 roll remaining:")
    for combination, probability in probabilities.items():
        print(f"- {combination}: {probability:.2%}")
    
    # Test with 2 rolls remaining
    probabilities = calculate_all_probabilities(dice_values, 2)
    print("\nWith 2 rolls remaining:")
    for combination, probability in probabilities.items():
        print(f"- {combination}: {probability:.2%}")
    
    # Test case 2: Almost Full House (3 of a kind + 1)
    dice_values = [3, 3, 3, 5, 1]
    print(f"\nTest case 2 - Almost Full House: {dice_values}")
    
    # Test with 1 roll remaining
    probabilities = calculate_all_probabilities(dice_values, 1)
    print("With 1 roll remaining:")
    for combination, probability in probabilities.items():
        print(f"- {combination}: {probability:.2%}")
    
    # Test case 3: Almost Escalera (1,2,3,4,6)
    dice_values = [1, 2, 3, 4, 6]
    print(f"\nTest case 3 - Almost Escalera: {dice_values}")
    
    # Test with 1 roll remaining
    probabilities = calculate_all_probabilities(dice_values, 1)
    print("With 1 roll remaining:")
    for combination, probability in probabilities.items():
        print(f"- {combination}: {probability:.2%}")

def test_edge_cases():
    """Test some edge cases for the probability calculations"""
    print("\n==== Testing Edge Cases ====")
    
    # Test case: Already have Generala
    dice_values = [4, 4, 4, 4, 4]
    print(f"\nAlready have Generala: {dice_values}")
    probabilities = calculate_all_probabilities(dice_values, 1)
    print("Probabilities (1 roll remaining):")
    for combination, probability in probabilities.items():
        print(f"- {combination}: {probability:.2%}")
    
    # Test case: Already have Full
    dice_values = [2, 2, 2, 5, 5]
    print(f"\nAlready have Full: {dice_values}")
    probabilities = calculate_all_probabilities(dice_values, 1)
    print("Probabilities (1 roll remaining):")
    for combination, probability in probabilities.items():
        print(f"- {combination}: {probability:.2%}")

if __name__ == "__main__":
    test_integration_with_dice()
    test_specific_dice_configurations()
    test_edge_cases()