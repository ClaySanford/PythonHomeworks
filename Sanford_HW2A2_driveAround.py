# -*- coding: utf-8 -*-
"""
Created by Clay Sanford
HW 2 Question 2 Response:
"""
def driveAround(directions):
    if len(directions) != 10:
        return False
    if directions.count('N') != directions.count('S'):
        return False
    if directions.count('E') != directions.count('W'):
        return False
    return True
"""
I feel like this uses a reasonable amount of included functions, while maintaining a nice bit of optimization. 
It's most likely that the lenght isn't 10 if it's truly random, and then north/south and east/west have an equal probability,
so their ordering doesn't reall matter.
"""