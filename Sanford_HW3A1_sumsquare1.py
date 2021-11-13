# -*- coding: utf-8 -*-
"""
Created by Clay Sanford
HW 3 Question 1 Response:
"""

def sumsquare1(n):
    return sum(i for i in range(1, n+1)) ** 2 - sum(list(map(lambda x : x ** 2, range(1, n + 1))))

"""I think this is what you want? I used map and lambda to square the digits before adding them. It's not nice code, and 
it's bulky, as I didn't want to put it on multiple lines, but it does what you specified, as far as I understood."""