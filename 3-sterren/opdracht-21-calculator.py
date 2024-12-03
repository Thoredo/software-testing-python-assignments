# TODO make whole numbers int instead of float
# TODO if user uses , for float numbers convert into .
# TODO let the user keep turning in numbers till they type stop
# TODO ability to continue with last result?


class Calculator:
    def add(self, number_1, number_2):
        return number_1 + number_2

    def subtract(self, number_1, number_2):
        return number_1 - number_2

    def multiply(self, number_1, number_2):
        return number_1 * number_2

    def divide(self, number_1, number_2):
        if number_2 == 0:
            return "Can't divide by 0"
        return number_1 / number_2


calculator = Calculator()
user_input = input(
    "What do you want to calculate? seperate your calculation with the spacebar ex: 1 + 1 : "
)

input_list = user_input.split(" ")
input_list[0] = float(input_list[0])
input_list[2] = float(input_list[2])
match input_list[1]:
    case "+":
        result = calculator.add(input_list[0], input_list[2])
    case "-":
        result = calculator.subtract(input_list[0], input_list[2])
    case "*":
        result = calculator.multiply(input_list[0], input_list[2])
    case "/":
        result = calculator.divide(input_list[0], input_list[2])

print(result)
