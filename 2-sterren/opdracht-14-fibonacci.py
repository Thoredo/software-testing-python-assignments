number_a = 0
number_b = 1

for i in range(15):
    print(number_a)
    number_a, number_b = number_b, number_a + number_b
