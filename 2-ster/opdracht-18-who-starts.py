import random

player_amount = int(input("How many players are playing? "))
player_names = []


for i in range(player_amount):
    player_name = input(f"What is the name for player {i+1}? ")
    player_names.append(player_name)

print(f"{random.choice(player_names).capitalize()} gets to start")
