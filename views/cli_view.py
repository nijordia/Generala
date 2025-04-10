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