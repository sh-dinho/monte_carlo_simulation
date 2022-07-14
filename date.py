# Write a program that reads in a number and prints the date that number of days from now in this format: Saturday, February 06, 2021.
# For example, if the user enters 150 the program should display “Saturday, February 06, 2021”

import datetime as dt

user_input = int(input("Enter a number: "))
today = dt.date.today()
date = today + dt.timedelta(days=user_input)
#display the date in this format: Saturday, February 06, 2021 (Saturday, February 06, 2021)
print(date.strftime("%A, %B %d, %Y"))
#display the date in this format: Saturday, February 06, 2021 (Saturday, February 06, 2021)
