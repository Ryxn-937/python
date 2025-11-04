import random
import math

names = input("Enter the names of invited guests (comma-separated): ")
name_list = [name.strip() for name in names.split(",")]
unique_names = list(set(name_list))
chosen_name = random.choice(unique_names)
reversed_name = chosen_name[::-1]
print("\n--- Birthday Name Game ---")
print("Chosen name (reversed):", reversed_name)
print("Total unique names:", len(unique_names))
print("Rounded square root of total:", round(math.sqrt(len(unique_names))))
