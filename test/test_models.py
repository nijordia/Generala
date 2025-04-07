from models.dice import Die, DiceSet



# Example 1: Using a single Die
print("==== Single Die Example ====")
d = Die()
print(f"Initial die value: {d.value}")
first_roll = d.roll()
print(f"After rolling: {d.value}")
second_roll = d.roll()
print(f"After rolling again: {d.value}")


# Example 2: Using a non-standard die (e.g., 10-sided die)
print("\n==== Non-standard Die Example ====")
d10 = Die(faces=10)
print(f"Initial 10-sided die value: {d10.value}")
first_roll_d10 = d10.roll()
print(f"After rolling 10-sided die: {d10.value}")


# Example 3: Using a set of dice (5 dice by default)
print("\n==== Dice Set Example ====")
dice_set = DiceSet()
print(f"Initial dice values: {dice_set.get_values()}")

# Roll all dice in the set
roll_results = dice_set.roll_all()
print(f"After rolling all dice: {dice_set.get_values()}")
print(f"Roll results: {roll_results}")

# String representation
print(f"\nString representation: {dice_set}")

# Example 4: Creating a custom dice set (3 dice with 8 faces each)
print("\n==== Custom DiceSet Example ====")
custom_dice = DiceSet(dice_count=3, faces=8)
print(f"Initial values: {custom_dice.get_values()}")
custom_dice.roll_all()
print(f"After rolling: {custom_dice}")




