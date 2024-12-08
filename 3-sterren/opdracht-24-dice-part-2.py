import random

dice_to_throw = input(
    "using the AdX notation please tell me how many dice we need to roll of how many sides: "
)

dice_thrown = []

adx_split = dice_to_throw.split("d")

dice_amount = int(adx_split[0])
dice_sides = int(adx_split[1])

print(f"rolling {dice_amount} dice with {dice_sides} sides now")

for i in range(dice_amount):

    die_roll = random.randint(1, dice_sides)
    dice_thrown.append(die_roll)

print(f"The total amount rolled is {sum(dice_thrown)}.")
