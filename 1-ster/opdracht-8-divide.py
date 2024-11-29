numbers = []

while len(numbers) < 3:
    try:
        number = int(input("Please give a number: "))
        if number == 0:
            print("You can't divide by 0 you doofus.")
        else:
            numbers.append(number)
    except ValueError:
        print("Please give a valid number and without decimals.")

print(round((numbers[0] / numbers[1]) / numbers[2], 4))
