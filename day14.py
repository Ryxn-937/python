import random
import math

names = input("Enter the names of customers who placed orders today (comma-separated): ")
name_list = [name.strip() for name in names.split(",")]
unique_names = list(set(name_list))
random.shuffle(unique_names)

total_participants = len(unique_names)
print(f"\nTotal unique participants: {total_participants}")

sqrt_participants = round(math.sqrt(total_participants))
print(f"Square root of participants (rounded): {sqrt_participants}")

if total_participants < 2:
    print("\nNot enough participants to pick 2 winners.")
else:
    winners = random.choices(unique_names, k=2)
    reversed_winners = [winner[::-1] for winner in winners]
    print("\n Lucky Draw Winners ")
    print(f"{reversed_winners[0]}")
    print(f"{reversed_winners[1]}")




