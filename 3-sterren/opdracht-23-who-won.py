player_amount = int(input("How many players are playing? "))
player_names_and_scores = {}

for i in range(player_amount):
    player_name = input(f"What is the name for player {i+1}? ")
    player_score = int(input("What is their score? "))
    player_names_and_scores[player_name] = player_score


winner = max(player_names_and_scores, key=player_names_and_scores.get)
print(f"{winner} wins!")
