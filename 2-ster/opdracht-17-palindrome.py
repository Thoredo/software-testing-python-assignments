user_input = input("Give me a word, lets see if its a palindrome. ")

if user_input == user_input[::-1]:
    print("Is palindrome.")
else:
    print("Is not palindrome.")
