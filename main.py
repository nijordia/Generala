from controllers.game_controller import GameController
from models.score import calculate_score

def main():
    """
    Main function to run the Generala game with interactive console input.
    """
    # Get player information
    print("=== Welcome to Generala ===")
    num_players = int(input("How many players? "))
    
    players = []
    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ")
        players.append(name)
    
    game = GameController(players)
    print(f"\nStarting Generala game with {len(players)} players: {', '.join(players)}")
    
    # Main game loop
    game_active = True
    while game_active:
        current_player = game.get_current_player()
        print(f"\n\n=== {current_player}'s turn ===")
        
        # Reset the dice for this turn
        game.dice_set.reset_throw_count()
        
        # First roll is automatic (all dice)
        throw_count, dice_values = game.roll_dice()
        print(f"Roll #{throw_count}: {dice_values}")
        
        # Player can make up to 3 throws total
        while throw_count < 3:
            # Show probabilities if there are rolls remaining
            probabilities = game.calculate_probabilities()
            if probabilities:
                print("\nProbabilities of achieving combinations:")
                for combination, probability in probabilities.items():
                    print(f"{combination}: {probability:.2%}")
                
                # If there's a best combination, suggest it
                best_combo = game.get_best_combination()
                if best_combo:
                    print(f"Recommendation: Try for {best_combo[0]} (probability: {best_combo[1]:.2%})")
            
            # Ask if player wants to roll again
            roll_again = input("\nRoll again? (y/n): ").lower().strip()
            if roll_again != 'y':
                break
            
            # Ask which dice to keep (by position)
            print("\nCurrent dice:", dice_values)
            keep_dice = input("Enter positions (0-4) of dice to KEEP (separated by spaces): ")
            
            # Convert input to indices to roll (those not kept)
            if keep_dice.strip():
                keep_indices = [int(i) for i in keep_dice.split()]
                roll_indices = [i for i in range(5) if i not in keep_indices]
            else:
                # Roll all dice if no input
                roll_indices = list(range(5))
            
            # Roll selected dice
            throw_count, dice_values = game.roll_dice(roll_indices)
            print(f"\nRoll #{throw_count}: {dice_values}")
        
        # Show available combinations that haven't been used yet
        available_combinations = game.get_available_combinations()
        print(f"\nAvailable combinations for {current_player}: {available_combinations}")
        
        # Check which combinations are valid with the current dice
        print("\nPossible scoring options with current dice:")
        valid_combinations = []
        for combo in available_combinations:
            try:
                # Calculate the score to validate if the combination can be formed
                rolls_remaining = 3 - throw_count
                score = calculate_score(combo, dice_values, rolls_remaining)
                print(f"- {combo}: {score} points")
                valid_combinations.append((combo, score))
            except ValueError:
                # The combination cannot be formed with current dice
                pass
        
        if not valid_combinations:
            print("No valid combinations with current dice. You must cross one out.")
        
        # Ask player which combination to score or cross out
        while True:
            if valid_combinations:
                print("\nValid combinations you can score:")
                for combo, score in valid_combinations:
                    print(f"- {combo}: {score} points")
                combo_choice = input("\nChoose a combination to score: ")
                
                # Check if selection is valid
                valid_combo_names = [combo for combo, _ in valid_combinations]
                if combo_choice in valid_combo_names:
                    score = game.score_combination(combo_choice)
                    print(f"\nScored {score} points for {combo_choice}")
                    break
                else:
                    print("Invalid choice. Please select a valid combination.")
            else:
                # No valid combinations available, must cross one out
                print("\nNo valid combinations with current dice. You must cross one out.")
                print("\nAvailable combinations to cross out:")
                for combo in available_combinations:
                    print(f"- {combo}")
                    
                combo_choice = input("\nChoose a combination to cross out: ")
                if combo_choice in available_combinations:
                    game.cross_out_combination(combo_choice)
                    print(f"Crossed out {combo_choice} for 0 points.")
                    break
                else:
                    print("Invalid choice. Please select from available combinations.")
        
        # End turn and move to next player
        game.next_turn()
        
        # Increase player index
        game.current_player_idx = (game.current_player_idx + 1) % len(game.players)
        
        # Display scores after each round
        scores = game.get_scores()
        print("\nCurrent scores:")
        for player, score in scores.items():
            print(f"{player}: {score}")
        
        # Check if game is over (all rounds played)
        if game.current_round > game.max_rounds:
            game_active = False
    
    # Game over, display final results
    print("\n\n=== GAME OVER ===")
    scores = game.get_scores()
    print("\nFinal scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")
    
    winners = game.get_winner()
    if len(winners) == 1:
        print(f"\nWinner: {winners[0]}! 🎉")
    else:
        print(f"\nTie between: {', '.join(winners)}! 🎉")

if __name__ == "__main__":
    main()