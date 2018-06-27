# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 15:44:21 2018

@author: ahorgan
"""
# Nested loop hashtag drawing
"""
for i in range(1,7):
    print("#", end=" ")
    for j in range(1, i+1):
        print(" ", end=" ")
    print("#", end=" ")
    print()

#Turtle Maze Drawing
import turtle
turtle.penup()
turtle.goto(100,100)
turtle.pendown()
for x in range (0,100):
    turtle.backware(30)

"""
#Nested loop pyramid drawing
n = eval(input("Enter a number from 1-15:"))
i = n*2-2
for x in range(1,n):
    for y in range(0,i):
        if(y < x):
            print(x-y, end=" ")
        else:
            print(" ", end=" ")
    print()