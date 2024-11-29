user_numbers = input("Please give 5 numbers seperated with the spacebar: ")
number_list = user_numbers.split(" ")

for i in range(len(number_list)):
    number_list[i] = int(number_list[i])

sorted_numbers = sorted(number_list, reverse=True)

print(sorted_numbers)
