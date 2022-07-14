# Write a program that reads in a number and prints the sum of all values from 1 up to the number.
# For example, if the user enters 5 the program should display 15.  15 is (1+2+3+4+5)

from numpy import number


Number = int(input("Enter a number: "))
Sum = 0
for i in range(1, Number + 1):
    Sum += i
print(Sum)

# Write a program that reads in numbers until a -1 is entered and prints the sum of all numbers entered.
#  For example, if the user enters 5 10 15 -1 the program should display 30 (Each number will be separated by a carriage return).  30 is (5+10+15)
number = int(input("Enter a number: "))
sum = 0
while number != -1:
    sum += number
    number = int(input("Enter a number: ")) 
print(sum)

