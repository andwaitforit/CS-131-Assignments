# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Calories Burned Program
time = 0
for x in range(10, 31, 5):
    cals = x * 4.2
    print("You've burned", cals, "in", x, "minutes!")

# Salary Increase Calculator
salary = .01
days = int(input("How many days would you like to work?"))
for x in range(1, days):
    salary *= 2
    print("For day", x, "you earned $", salary, "dollars!")

# Tuition Increase Calculator
tuition = 8000
increase = .03
for x in range(0, 5):
   tuition +=(tuition * increase)
   print(round(tuition, 2))


# Factorial Calculator
factor = eval(input("What number would you like to factor?"))+1
factored = 1

if factor - 1 >0:
    for x in range(1, factor):
        factored *= x
        if x == factor - 1:
                print(factored)
else:
    print("Please input positive number.")
 