# number = input("give number: ")
# if number.isdigit():
#     print("is number")
# else:
#     print("not a number")

try:
    number1 = float(input("give number: "))
    number2 = float(input("give number 2: "))
    print("Is an int")
except ValueError:
    print("Not an int")
