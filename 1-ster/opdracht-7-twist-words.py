def reverse_string(a_string):
    return a_string[::-1]


user_input = input("Type any word: ")
reversed_word = reverse_string(user_input)
print(f"The reversed word is {reversed_word}")
