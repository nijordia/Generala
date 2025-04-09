def calculate_score(combination, dice, rolls_remaining):
    """
    Calculate the score for a given combination or number selection.
    :param combination: A string representing the achieved combination 
                        (e.g., "Generala", "Pócker", "Full", "Escalera", "Sixes", "Fives", etc.).
    :param dice: A list of integers representing the dice outcomes.
    :param rolls_remaining: An integer representing the number of rolls the player has left (0, 1 or 2).
    :return: An integer representing the total points for the turn.
    """
    # Define the base scores for combinations
    combination_scores = {
        "Generala": 50,
        "Generala Doble": 100,
        "Pócker": 40,
        "Full": 30,
        "Escalera": 25
    }
    
    score = 0

    # Check if the combination is a predefined one
    if combination in combination_scores:
        score = combination_scores[combination]
        # Apply the bonus rule for achieving the combination on the first roll
        if rolls_remaining == 2:
            score += 5
    elif combination in ["Sixes", "Fives", "Fours", "Threes", "Twos", "Ones"]:
        # Handle scoring for individual number combinations
        number = {"Ones": 1, "Twos": 2, "Threes": 3, "Fours": 4, "Fives": 5, "Sixes": 6}[combination]
        score = number * dice.count(number)
    else:
        raise ValueError(f"Invalid combination: {combination}")

    return score