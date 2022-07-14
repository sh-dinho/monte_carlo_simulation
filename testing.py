# Write a program that reads in a number and prints the either Small, Medium or Large depending on if the number is bellow 100 or above 200.
# For example, if the user enters 150 the program should display “Medium”
# Another example, is if the user enters 50 the program should display 

from numpy import number


number = int(input("Enter a number: "))
if number < 100:
    print("Small")
# if the number is above 100 and bellow 200
elif number > 100 and number < 200:
    print("Medium")
# if the number is above 200 
elif number > 200:
    print("Large")
else:
    print("Invalid")
# Write a program that reads in a number and prints the either Small, Medium or Large depending on if the number is bellow 100 or above 200.