# Command-line interface view for the application
import time
from models.game_state import Scoreboard
from models.dice import DiceSet

def display_welcome_message():
    """
    Display the welcome message for the Generala game with your custom ASCII title.
    """
    # Stylish representation of the Generala name
    print("\n╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┬  ┌─┐")
    print("║ ╦├┤ │││├┤ ├┬┘├─┤│  ├─┤")
    print("╚═╝└─┘┘└┘└─┘┴└─┴ ┴┴─┘┴ ┴\n")
    print("Welcome to Generala! 🎲\n")
    print("A traditional Argentine dice game of luck and strategy.")
    print("------------------------------------------------------")
    print("Roll the dice, strategize, and aim for the highest score!")
    print("Will you achieve the coveted Generala or play it safe?")
    print("It's time to find out!")
    print("------------------------------------------------------")

def display_rules():
    """
    Display the rules and instructions for playing Generala.
    """
    print("\n🔹 How to Play Generala 🔹")
    print("------------------------------------------------------")
    print("🎲 **Objective**: Score the most points by achieving dice combinations!")
    print("\n🔸 **Gameplay**:")
    print("  1. Each player takes turns rolling 5 dice.")
    print("  2. You can re-roll any dice up to **2 additional times** per turn.")
    print("  3. After your third roll, choose a valid combination to score points.")
    print("\n🔸 **Scoring**:")
    print("  - Combinations include Generala, Pócker, Full, Escalera, and more.")
    print("  - Specific combinations yield different point values.")
    print("  - You must choose a combination (or sacrifice one for 0 points).")
    print("\n🔸 **End of the Game**:")
    print("  - The game ends when all players have filled their scoreboards.")
    print("  - The player with the **highest total score** wins!")
    print("------------------------------------------------------")

def display_scoreboard(scoreboard):
    """
    Display the scoreboard as a formatted table with borders.
    :param scoreboard: An instance of the Scoreboard class.
    """
    print("\n+-------------------+--------+-----------+")
    print("| Combination       | Score  | Status    |")
    print("+-------------------+--------+-----------+")
    for combination, details in scoreboard.combinations.items():
        score = details["score"] if details["score"] is not None else "-"
        status = "Played" if details["played"] else "Available"
        print(f"| {combination:<17} | {score:<6} | {status:<9} |")
    print("+-------------------+--------+-----------+")


def print_dice(dice):
    """
    Print the five dice with a 2-second delay for suspense.
    :param dice: A list of integers representing the dice outcomes.
    """
    print("\nRolling the dice...")
    time.sleep(2)  # Wait for 2 seconds before showing the result
    print("+---+---+---+---+---+")
    print("|", " | ".join(map(str, dice)), "|")
    print("+---+---+---+---+---+")

def display_available_combinations(combinations_data):
    """
    Display a board of combinations with colored rows to indicate availability, based on provided data.
    :param combinations_data: A list of dictionaries, where each dictionary contains:
                              - 'id': Combination number for player input.
                              - 'name': Name of the combination.
                              - 'available': Availability status (True/False).
                              - 'potential_score': Potential score for the combination.
    """
    print("\n+-----+-------------------+----------------+")
    print("| No. | Combination       | Potential Score|")
    print("+-----+-------------------+----------------+")

    for combo in combinations_data:
        # Set row color based on availability
        color = "\033[92m" if combo['available'] else "\033[91m"  # Green for available, red for unavailable
        reset_color = "\033[0m"

        # Print the formatted row with color
        print(f"{color}| {combo['id']:<3} | {combo['name']:<17} | {combo['potential_score']:<14} |{reset_color}")

    print("+-----+-------------------+----------------+")

def prompt_turn_action():
    """
    Prompt the user to decide whether to end their turn or re-roll some dice.
    :return: A tuple (action, selected_indices), where:
             - action is a string ('end_turn' or 're_roll').
             - selected_indices is a list of integers representing the dice to re-roll (empty if 'end_turn').
    """
    while True:
        print("\nWhat would you like to do?")
        print("1. End your turn")
        print("2. Re-roll some dice")
        try:
            choice = int(input("Enter the number of your choice: "))
            if choice == 1:
                return "end_turn", []
            elif choice == 2:
                return "re_roll", prompt_dice_selection()
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")


def prompt_dice_selection():
    """
    Prompt the user to select which dice to re-roll.
    :return: A list of indices representing the dice to re-roll.
    """
    print("\nEnter the indices of the dice you want to re-roll (e.g., 0 2 4):")
    user_input = input("Your selection: ")
    try:
        selected_indices = list(map(int, user_input.split()))
        return selected_indices
    except ValueError:
        print("Invalid input. Please enter space-separated indices (e.g., 0 2 4).")
        return prompt_dice_selection()

def display_probabilities(probabilities):
    """
    Display the probabilities of achieving playable combinations.
    :param probabilities: A list of dictionaries, where each dictionary contains:
                           - 'name': Name of the combination.
                           - 'probability': Probability of achieving the combination.
    """
    print("\n+-------------------+-----------------+")
    print("| Combination       | Probability (%) |")
    print("+-------------------+-----------------+")
    for combo in probabilities:
        print(f"| {combo['name']:<17} | {combo['probability'] * 100:<15.2f} |")
    print("+-------------------+-----------------+")

def prompt_player_turn_options(player_name, dice_rolled, rolls_remaining, combination_chosen):
    """
    Prompt the user with options for their turn and validate the input.
    :param player_name: The name of the active player.
    :param dice_rolled: A boolean indicating if the dice have been rolled.
    :param rolls_remaining: An integer representing the number of rolls left.
    :param combination_chosen: A boolean indicating if a combination has been chosen or crossed out.
    :return: The user's choice as an integer.
    """
    print(f"\n🎲 {player_name}'s Turn 🎲")
    print("------------------------------------------------------")
    print("What would you like to do?")
    print("1. Throw dice" if not dice_rolled else "1. Throw dice (Already rolled)")
    print("2. View your scoreboard")
    print("3. View probabilities" if dice_rolled else "3. View probabilities (Unavailable)")
    print("4. Re-roll dice" if dice_rolled and rolls_remaining > 0 else "4. Re-roll dice (Unavailable)")
    print("5. Choose combination for scoring" if dice_rolled else "5. Choose combination for scoring (Unavailable)")
    print("6. Cross out combination and get 0 points" if dice_rolled else "6. Cross out combination (Unavailable)")
    print("7. View game instructions")
    print("8. End turn" if dice_rolled and combination_chosen else "7. End turn (Unavailable)")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if choice in range(1, 9):
                return choice
            else:
                print("Invalid choice. Please select a valid option (1-8).")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")