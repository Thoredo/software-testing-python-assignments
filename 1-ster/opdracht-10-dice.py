import random

number_of_dice = int(input("How many dice do you want to roll? "))

dice_thrown = []

print(f"rolling {number_of_dice} dice now")

for i in range(number_of_dice):

    die_roll = random.randint(1, 6)
    dice_thrown.append(die_roll)

for die in dice_thrown:
    print(die)

print(f"The total amount rolled is {sum(dice_thrown)}.")
