# -*- coding: utf-8 -*-
"""
Created by Clay Sanford
HW 2 Question 1 Response:
"""
def digitSquare(base):
    k = 0
    output = 0
    while base != 0:
        output = output + (((base%10)**2) * (10 ** k)) #Adds the last digit squared to the output, with k tracking what position it needs to be added to.
        k +=1                                           #Increments k by 1
        if (base%10)**2 > 9:                            #If the previously added number is two digits,
            k += 1                                      #Increments k by an extra one, for spacing.
        base = base // 10                               #Base is the intDivision by 10, to remove the last digit
    return output

"""
As a note, I had previously done this with more python functions, but it was **SIGNIFICANTLY LESS EFFICIENT**
However, just to show how you could incorporate an included function into this (even if would increase runtime), I have included my first attempt below.
It's nowhere near as elegant or quick, but I suppose neither of these are important if you're really looking for an understanding of python

def digitSquare(base):
    numArray = []       # Declares an array to break the base number into different digits
    k = 0               #k is just an integer to help keep track of two-digit squares
    output = 0          # Declares an int for the output 
    while base != 0: 
        numArray.append(base%10) # Add the last digit of the base to the array. 
        base = base // 10 # Remove the last digit from the base
    digitCount = len(numArray) # Creates a variable for the length of numArray
    for i in range(digitCount):
        numArray[i] = numArray[i] ** 2 # Square every individual digit
    for j in range(digitCount):
        output = output + numArray[j] * (10 ** (j + k)) #Adds together all the numbers at their appropriate power of 10. j and k need to start at 0. Could be done with a .pop function
        if numArray[j] > 9: 
            k += 1 #Increment K in the case of double-digit squares
    return output   #As a note, I could likely merge this into one step, omiting the array completely. 
"""