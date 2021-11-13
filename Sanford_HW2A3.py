# -*- coding: utf-8 -*-
"""
Created by Clay Sanford
HW 2 Question 3 Response:
"""
def sumSquares(inputNum):  #This function finds the sum of the squares.
    output = 0 #Declares a variable for the output
    for i in range(inputNum): #For loop, from 0 to the given value - 1. 
        output += (i+1) ** 2 #Squares, then sums
    return(output) 

def squareSums(inputNum): #This function finds the square of the sums.
    output = 0 #Declares a variable for the output
    for i in range(inputNum): # For loop, from 0 to the given value - 1. 
        output += (i+1) #Adds 1, 2, ... the input.
    return(output ** 2) #Squares the sums, then returns the squared sums.

def ssDiff(inputNum): #This function finds the difference between the square of the sums and the sum of the squares. 
    return(squareSums(inputNum) - sumSquares(inputNum)) #Returns the difference between the two functions.
    
while True: #This isn't the most proper, but it does what I want it to.
    findVal = int(input("Please enter the number you would like to find the difference betweeen the square of sums and the sum of squares: "))
    print(ssDiff(findVal)) #Prints the return from the ssDiff call.
    check = str(input("Would you like to find the difference for another value? (Y/N): "))
    if check == 'N' or check == 'n': #If the person said no,
        print('Goodbye!')
        break #Ends the loop.
"""
It feels almost like I'm making a mistake here; every other programming assignment has been to create a function, 
whereas this is simply make a program. I also am unsure if this is how you wanted the response. I could have had the 
program just run once, but I like loops. 
"""