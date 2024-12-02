user_not_done = True
user_wishlist = []

while user_not_done:
    user_input = input("What do you want to add to your wishlist? ")
    if user_input.upper() == "READY":
        user_not_done = False
        break
    else:
        user_wishlist.append(user_input)

user_wishlist.sort()
print(user_wishlist)
