from ..models.dice import Die


print("==== Single Die Example ====")
d = Die()
print(f"Initial die value: {d.value}")
first_roll = d.roll()
print(f"After rolling: {d.value} (Expected: {first_roll})")
second_roll = d.roll()
print(f"After rolling again: {d.value} (Expected: {second_roll})")







