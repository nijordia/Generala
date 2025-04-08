from math import comb

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

def calculate_full_probability(dice, rolls_remaining):
    """
    Calculate the probability of achieving Full (three-of-a-kind and two-of-a-kind) 
    based on the current dice and rolls remaining.
    :param dice: A list of integers representing the outcomes of the dice.
    :param rolls_remaining: An integer representing the number of rolls left (1 or 2).
    :return: A float representing the probability of achieving Full.
    """
    # Count the occurrences of each number
    counts = {i: dice.count(i) for i in range(1, 7)}
    
    # Extract the maximum count (most repeated number) and the second-highest count
    sorted_counts = sorted(counts.values(), reverse=True)
    max_matches = sorted_counts[0]  # Number of dice in the largest group
    second_max_matches = sorted_counts[1]  # Number of dice in the second-largest group

    # Remaining dice to match
    if max_matches == 3:
        remaining_dice = 2 - second_max_matches  # Need to complete the pair
    elif max_matches == 2:
        remaining_dice = 3  # Need to complete three-of-a-kind and pair
    else:
        remaining_dice = 5  # Starting with no useful matches

    # Handle cases based on rolls_remaining
    if rolls_remaining == 1:
        # Case 1: One roll remaining
        if max_matches == 3 and second_max_matches == 2:
            # Already a Full House
            return 1.0
        # Probability formula for one roll: (1/6)^remaining_dice
        return (1/6) ** remaining_dice
    elif rolls_remaining == 2:
        # Case 2: Two rolls remaining
        total_probability = 0

        # Loop through possible outcomes of the first re-roll
        for first_roll_matches in range(remaining_dice + 1):  # 0 to remaining_dice
            # Probability of achieving `first_roll_matches` in the first re-roll
            prob_first_roll = calculate_binomial_probability(remaining_dice, first_roll_matches)
            
            # Remaining dice after the first roll
            dice_left = remaining_dice - first_roll_matches
            
            # Probability of achieving Full in the second roll
            prob_second_roll = (1/6) ** dice_left

            # Combine probabilities for this outcome
            total_probability += prob_first_roll * prob_second_roll

        return total_probability

def calculate_escalera_probability(dice, rolls_remaining):
    """
    Calculate the probability of achieving Escalera (Straight) 
    based on the current dice and rolls remaining.
    :param dice: A list of integers representing the outcomes of the dice.
    :param rolls_remaining: An integer representing the number of rolls left (1 or 2).
    :return: A float representing the probability of achieving Escalera.
    """
    # Identify the gaps in the straight
    straight_1 = {1, 2, 3, 4, 5}
    straight_2 = {2, 3, 4, 5, 6}
    current_dice = set(dice)

    # Count missing numbers for both possible straights
    missing_1 = len(straight_1 - current_dice)  # Gaps for [1, 2, 3, 4, 5]
    missing_2 = len(straight_2 - current_dice)  # Gaps for [2, 3, 4, 5, 6]
    gaps = min(missing_1, missing_2)  # Minimum gaps for a valid Escalera

    # Handle cases based on rolls_remaining
    if rolls_remaining == 1:
        # Case 1: One roll remaining
        return (1/6) ** gaps
    elif rolls_remaining == 2:
        # Case 2: Two rolls remaining
        total_probability = 0

        # Loop through possible outcomes of the first re-roll
        for first_roll_matches in range(gaps + 1):  # 0 to gaps
            # Probability of achieving `first_roll_matches` in the first re-roll
            prob_first_roll = calculate_binomial_probability(gaps, first_roll_matches)
            # Remaining gaps after the first re-roll
            gaps_left = gaps - first_roll_matches
            # Probability of completing Escalera in the second roll
            prob_second_roll = (1/6) ** gaps_left
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

# Central function
def calculate_all_probabilities(dice, rolls_remaining):
    # Ensure the input is valid
    if len(dice) != 5 or not all(1 <= die <= 6 for die in dice):
        raise ValueError("Invalid input! The dice list must contain exactly five values between 1 and 6.")
    if rolls_remaining not in [1, 2]:
        raise ValueError("rolls_remaining must be either 1 or 2.")
    # Calculate probabilities for each combination
    probabilities = {
        "Generala": calculate_generala_probability(dice, rolls_remaining),
        "Pócker": calculate_poker_probability(dice, rolls_remaining),
        "Full": calculate_full_probability(dice, rolls_remaining),
        "Escalera": calculate_escalera_probability(dice, rolls_remaining)
    }
    return probabilities
