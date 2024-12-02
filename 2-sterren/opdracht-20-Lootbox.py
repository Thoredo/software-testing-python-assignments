import random

total_result = {"Common": 0, "Uncommon": 0, "Rare": 0, "Epic": 0, "Legendary": 0}

for i in range(1000):
    result = random.randint(1, 100)

    if result < 60:
        total_result["Common"] += 1
    elif result < 80:
        total_result["Uncommon"] += 1
    elif result < 90:
        total_result["Rare"] += 1
    elif result < 99:
        total_result["Epic"] += 1
    else:
        total_result["Legendary"] += 1

print(total_result)
