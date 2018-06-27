# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 19:32:47 2018

@author: ahorgan
"""

#Insurance Calculator
rCost = eval(input("How much is the cost for home replacement?"))
insurance = rCost * .8
print(insurance)


#Math Quick
from random import *
comp1 = randint(10,150)
comp2 = randint(90, 250)
compSum = comp1 + comp2
print(comp1, "+", comp2, "= ?")
userAnswer = eval(input("What is the sum of these two numbers?"))
if userAnswer == compSum:
    print("Correct!")
else:
    print("Incorrect, it's sum is:", compSum)






#generate computer number and take user input
from random import *
compInput = randint(0,2)
userInput = input("Rock, paper, scissors, SHOOT!").lower()
print(userInput)

#Array to hold rps values
rpsArray = ["paper", "scissors", "rock"]

#assign number to input
for i in range(0,3):
    if userInput == rpsArray[i]:
        newUser = i
        #print(newUser)
        
#run game simulation
if newUser == compInput:
    print("Computer chooses:", rpsArray[compInput], "It's a draw!")
elif newUser != 0 and compInput != 0:
    if newUser > compInput:
        print("Computer chooses:", rpsArray[compInput], "You won!")
    else:
        print("Computer chooses:", rpsArray[compInput], "You lost :(")
else:
    if compInput == 0:
        print("Computer chooses:", rpsArray[compInput], "You lost :(")
    else:
        print("Computer chooses:", rpsArray[compInput], "You won!")

#print(compInput)

        