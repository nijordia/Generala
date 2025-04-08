from math import comb

# Input
dice = [1,2,3,4,5,6] # Outcome of five 6-sided dice
rolls_remaining = 2 # Number of rolls remaining

# Individual functions for each combination
def calculate_generala_probability(dice, rolls_remaining):
    """
    Calculate the probability of achieving Generala based on the current dice and rolls remaining.
    :param dice: A list of integers representing the outcomes of the dice.
    :param rolls_remaining: An integer representing the number of rolls left (1 or 2).
    :return: A float representing the probability of achieving Generala.
    """
    # Count the occurrences of each number
    counts = {i: dice.count(i) for i in range(1, 7)}
    
    # Find the maximum count (most repeated number)
    max_matches = max(counts.values())
    # Remaining dice to match
    remaining_dice = 5 - max_matches
    # Handle cases based on rolls_remaining
    if rolls_remaining == 1:
        # Case 1: One roll remaining
        return (1/6) ** remaining_dice
    elif rolls_remaining == 2:
        # Case 2: Two rolls remaining
        total_probability = 0
        # Loop through possible outcomes of the first re-roll
        for new_matches in range(remaining_dice + 1):  # 0 to remaining_dice
            # Probability of achieving `new_matches` in the first re-roll
            prob_first_roll = calculate_binomial_probability(remaining_dice, new_matches)
            # Remaining dice after the second roll
            dice_left = remaining_dice - new_matches
            # Probability of achieving Generala in the third roll
            prob_second_roll = (1/6) ** dice_left
            # Combine probabilities for this outcome
            total_probability += prob_first_roll * prob_second_roll

        return total_probability   

def calculate_binomial_probability(n, k):
    """
    Calculate the probability of achieving exactly k matches from n dice.
    :param n: Number of dice being re-rolled.
    :param k: Number of matches needed.
    :return: A float representing the binomial probability.
    """
    # Binomial probability formula: (n choose k) × (1/6)^k × (5/6)^(n-k)
    binomial_coeff = comb(n, k)
    probability = binomial_coeff * (1/6)**k * (5/6)**(n-k)
    return probability

def calculate_poker_probability(dice, rolls_remaining):
    """
    Calculate the probability of achieving Pócker (four of a kind) based on the current dice and rolls remaining.
    :param dice: A list of integers representing the outcomes of the dice.
    :param rolls_remaining: An integer representing the number of rolls left (1 or 2).
    :return: A float representing the probability of achieving Pócker.
    """
    # Count the occurrences of each number
    counts = {i: dice.count(i) for i in range(1, 7)}
    
    # Find the maximum count (most repeated number)
    max_matches = max(counts.values())
    # Remaining dice to match for Pócker
    remaining_dice = 4 - max_matches
    # Handle cases based on rolls_remaining
    if rolls_remaining == 1:
        # Case 1: One roll remaining
        return (1/6) ** remaining_dice
    elif rolls_remaining == 2:
        # Case 2: Two rolls remaining
        total_probability = 0
         # Loop through possible outcomes of the first re-roll
        for new_matches in range(remaining_dice + 1):  # 0 to remaining_dice
            # Probability of achieving `new_matches` in the first re-roll
            prob_first_roll = calculate_binomial_probability(remaining_dice, new_matches)
            # Remaining dice after the first roll
            dice_left = remaining_dice - new_matches
            # Probability of achieving Pócker in the second roll
            prob_second_roll = (1/6) ** dice_left
            # Combine probabilities for this outcome
            total_probability += prob_first_roll * prob_second_roll

        return total_probability

def calculate_two_rolls_poker_probability(max_matches, counts):
    """
    Calculate the probability of achieving Pócker in two rolls.
    :param max_matches: The number of dice that currently match.
    :param counts: A dictionary of counts for each number (1 to 6).
    :return: A float representing the probability of achieving Pócker in two rolls.
    """
   


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
    if rolls_remaining not in [1, 2]:
        raise ValueError("rolls_remaining must be either 1 or 2.")
    # Calculate probabilities for each combination
    probabilities = {
        "Generala": calculate_generala_probability(dice),
        "Pócker": calculate_poker_probability(dice),
        "Full": calculate_full_probability(dice),
        "Escalera": calculate_escalera_probability(dice)
    }
    return probabilities
