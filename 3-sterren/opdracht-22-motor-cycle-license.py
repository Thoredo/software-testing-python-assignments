from datetime import datetime

today = datetime.now()

date_of_birth_input = input("What is your date of  birth (YYYY-MM-DD): ")

date_of_birth = datetime.strptime(date_of_birth_input, "%Y-%m-%d")

age_in_years = today.year - date_of_birth.year
if (today.month, today.day) < (date_of_birth.month, date_of_birth.day):
    age_in_years -= 1

print(f"Your age is {age_in_years}")
print(
    "For motorcycles in the Netherlands there is 3 licenses from low engine power to high: A1, A2, A"
)

if age_in_years < 17:
    print("you are too young for anything with licenses")
elif age_in_years == 17:
    print(
        "In category A1 you can start your drivers lessons. And theory test for all 3 categories"
    )
elif age_in_years == 18:
    print(
        "In category A1 you can do all 3 things. And theory test for the other 2 categories"
    )
elif age_in_years == 19:
    print(
        "If you already own a license category A1 you can start drivers lessons for A2"
    )
elif age_in_years == 20:
    print("You can do all 3 things for Category A1 and A2")
elif 21:
    print("You can do all 3 things for all 3 categories")
