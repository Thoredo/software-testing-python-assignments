election_results = {}
election_running = True

while election_running:
    user_vote = input("Who do you want to vote for? ")
    if user_vote.upper() == "UITSLAG":
        election_running = False
        break
    if user_vote in election_results:
        election_results[user_vote] += 1
    else:
        election_results[user_vote] = 1

winner = max(election_results, key=election_results.get)
print(f"{winner} wins, with {election_results[winner]} votes")
