"""
File: sum.py
Author: Your Name
Date: 2024-03-19
Description: A program that asks for user input, n, and calculates the
             sum of numbers from 1 to n using an accumulator variable.
"""


sum = 0 
n = int(input("Enter number: "))
for counter in range(1, n+1):
    if counter <= n:
        sum = sum + counter  # I update accumaltion variable sum evrytime
        counter = counter + 1    # to know whne i need ot stop looping, tilll i get the point where n is less than 1
    else:
        print(sum)
print(sum)


    

