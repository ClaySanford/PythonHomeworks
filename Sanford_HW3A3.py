# -*- coding: utf-8 -*-
"""
Created by Clay Sanford
HW 3 Question 3 Response:
"""

w = open("test.txt", 'w') #Creates the file as write
for i in range(1, 4): #Adds the first 3 lines.
    w.write("This is line " + str(i) + '\n')
w.close() #Closes the write

r = open("test.txt", 'r') #Opens the file, as read 
print(r.readline()) #Reads the first line
print(r.readline()) #Reads the sceond line
r.close() #Closes the read.

w = open("test.txt", 'a') #Opens an append
w.write("This is the fourth line") #Writes the fourth line
w.close() #Closes the append

r = open("test.txt", 'r') #Opens a read
allLines = r.readlines(); #Saves all lines as a list
for i in allLines[2:]: #Prints all lines, except for the first two (they've already been printed)
    print(i)
r.close() #Closes the file

"""This gave me a surprising amount of trouble. Either I would re-read the first two lines, or I simply wouldn't read
the last two. The closest compromise I found is to simply hard-code ignoring the first two lines, using list slicing."""
