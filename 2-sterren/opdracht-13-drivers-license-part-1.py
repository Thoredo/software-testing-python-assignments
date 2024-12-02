from datetime import datetime

today = datetime.now()

date_of_birth_input = input("What is your date of  birth (YYYY-MM-DD): ")

date_of_birth = datetime.strptime(date_of_birth_input, "%Y-%m-%d")

age_in_days = today - date_of_birth

age_in_years = age_in_days.days // 365

if age_in_years >= 18:
    print(f"You are {age_in_years} years old, and are allowed to drive.")
else:
    print(f"You are {age_in_years} years old, and are not allowed to drive.")
