from models.dice import Die, DiceSet


 # run using: python -m test.test_models


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


# Example 3: Using a set of dice with throw tracking
print("\n==== Dice Set with Throw Tracking Example ====")
dice_set = DiceSet()
print(f"Initial state: Throw count = {dice_set.throw_count}, Values = {dice_set.get_values()}")

# First roll (all dice)
throw_num, dice_values = dice_set.roll_all()
print(f"After first roll: Throw #{throw_num}, Values = {dice_values}")

# Second roll (selective - roll dice at indices 0, 2, 4)
selected_indices = [0, 2, 4]
print(f"Rolling selected dice at indices {selected_indices}")
throw_num, dice_values = dice_set.roll_selected(selected_indices)
print(f"After second roll: Throw #{throw_num}, Values = {dice_values}")


# Third roll (selective - roll dice at indices 1, 3)
selected_indices = [1, 3]
print(f"Rolling selected dice at indices {selected_indices}")
throw_num, dice_values = dice_set.roll_selected(selected_indices)
print(f"After third roll: Throw #{throw_num}, Values = {dice_values}")

# Try a fourth roll (should hit the maximum and not change dice)
print("\nAttempting fourth roll (should not roll due to max throws):")
throw_num, dice_values = dice_set.roll_all()
print(f"After attempted fourth roll: Throw #{throw_num}, Values = {dice_values}")

# Reset throw count and roll again
print("\nResetting throw count:")
dice_set.reset_throw_count()
throw_num, dice_values = dice_set.roll_all()
print(f"After reset and roll: Throw #{throw_num}, Values = {dice_values}")