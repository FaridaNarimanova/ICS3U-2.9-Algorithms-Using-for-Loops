"""
File: factorial.py
Author: Your Name
Date: 2024-03-19
Description: A program that asks for user input, n, and calculates the
             factorial n! outputting the final value.
"""
#I ask uswe for the n number whihc defines the starting number
n = int(input("numb: "))
# I assign numb to 1 since by multipling number by 0 i get zero, so numb is 1
numb = 1
# i is the variable in which value changes as my integer goes through range, so everytyme it goes through body, it changes 
# n is starting number
# 0 i the number i will get to
# - 1 i subtract n everytime
for i in range (n, 1 , - 1 ):
    numb *= i  
print(numb)
