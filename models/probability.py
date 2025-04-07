# Input
dices = [1,2,3,4,5,6] # 6-sided dice

# Individual functions for each combination
def calculate_generala_probability(dice):
    # Logic to calculate Generala probability
    pass

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
    probabilities = {
        "Generala": calculate_generala_probability(dice),
        "Pócker": calculate_poker_probability(dice),
        "Full": calculate_full_probability(dice),
        "Escalera": calculate_escalera_probability(dice)
    }
    return probabilities
