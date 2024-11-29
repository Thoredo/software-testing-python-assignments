import datetime

name = input("Hello what is your name? ")
age = int(input("What is your age? "))

today = datetime.date.today()

year = today.year

years_till_100 = 100 - age

print(f"You will be 100 in the year: {year + years_till_100}")

# Code can be 1 year off if the users birthday of this year has not happened yet.
