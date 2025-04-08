# Input
dice = [1,2,3,4,5,6] # 6-sided dice

# Individual functions for each combination
def calculate_generala_probability(dice):
    """
    Calculate the probability of achieving a Generala with five dice.
    :param dice: A list of integers representing the outcomes of the five dice.
    :return: A float representing the probability of Generala.
    """
    # Count the occurrences of each number
    counts = {i: dice.count(i) for i in range(1, 7)}

    # Find the maximum count (the most repeated number in the dice)
    max_matches = max(counts.values())

    # Calculate the number of dice that need to match
    remaining_dice = 5 - max_matches

    # Calculate the probability: (1/6)^remaining_dice
    probability = (1/6) ** remaining_dice

    return probability

def calculate_poker_probability(dice):
    # Logic to calculate Pócker probability
    pass

def calculate_full_probability(dice):
    # Logic to calculate Full probability
    pass

def calculate_escalera_probability(dice):
    # Logic to calculate Escalera probability
    pass

# Central function
def calculate_all_probabilities(dice):
    # Ensure the input is valid
    if len(dice) != 5 or not all(1 <= die <= 6 for die in dice):
        raise ValueError("Invalid input! The dice list must contain exactly five values between 1 and 6.")
    # Calculate probabilities for each combination
    probabilities = {
        "Generala": calculate_generala_probability(dice),
        "Pócker": calculate_poker_probability(dice),
        "Full": calculate_full_probability(dice),
        "Escalera": calculate_escalera_probability(dice)
    }
    return probabilities
