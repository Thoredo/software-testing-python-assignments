user_input = int(input("Give a number: "))

result = 1

while user_input > 0:
    result *= user_input
    user_input -= 1

print(result)
