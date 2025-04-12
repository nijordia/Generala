from controllers.game_controller import GameController

def main():
    """
    Main function to run the Generala game.
    """
    # Setup fame with players

    players = ["Alice", "Bob"]
    game = GameController(players)

    print(f"Starting Generala game with {len(players)} players: {', '.join(players)}")

    # Example of a single turn 
    current_player = game.get_current_player()
    print(f"It's {current_player}'s turn.")

    # First roll
    throw_count, dice_values = game.roll_dice()
    print(f"Roll #{throw_count}: {dice_values}")

    # Calculate probabilities
    probabilities = game.calculate_probabilities()
    print("\nProbabilities of achieving combinations:")
    for combination, probability in probabilities.items():
        print(f"{combination}: {probability:.2%}")
    
    
    # Second roll (keeping, for example, the first two dice)
    throw_count, dice_values = game.roll_dice([2, 3, 4])
    print(f"\nRoll #{throw_count} (keeping dice at positions 0,1): {dice_values}")
    
    # Updated probabilities
    probabilities = game.calculate_probabilities()
    print("\nUpdated probabilities:")
    for combination, probability in probabilities.items():
        print(f"{combination}: {probability:.2%}")
    
    # List available combinations
    available_combinations = game.get_available_combinations()
    print(f"\nAvailable combinations for {current_player}: {available_combinations}")
    
    # Score a combination (for example, the first available one)
    if available_combinations:
        combination = available_combinations[0]
        score = game.score_combination(combination)
        print(f"\nScored {score} points for {combination}")
    
    # End turn and move to next player
    game.next_turn()
    current_player = game.get_current_player()
    print(f"\nNext turn: {current_player}")
    
    # Display scores
    scores = game.get_scores()
    print("\nCurrent scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")

if __name__ == "__main__":
    main()