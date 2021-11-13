# -*- coding: utf-8 -*-
# Made by Clay Sanford
# CS 391-950
# Question 3 of HW 1

def book(readList):
    listLength = len(readList)
    if listLength == 0: #I would love to use a switch case for this, as they're significantly more efficient than stacking if statements. Oh well. 
        return("no one has read this")
    if listLength == 1:
        return(readList[0] + " has read this")
    if listLength == 2:
        return(readList[0] + " and " + readList[1] + " have read this")
    if listLength == 3:
        return(readList[0] + ", " + readList[1] + " and " + readList[2] + " have read this")
    if listLength > 3:
        return(readList[0] + ", " + readList[1] + " and " + str(listLength - 2) + " others have read this")
    return("Your entry could not be parsed.")