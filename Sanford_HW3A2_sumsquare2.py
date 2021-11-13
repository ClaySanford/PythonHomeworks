# -*- coding: utf-8 -*-
"""
Created by Clay Sanford
HW 3 Question 2 Response:
"""
from functools import reduce
import operator
def sumsquare2(n):
    return reduce(operator.add, range(1,n+1)) ** 2 - reduce(operator.add, (map(lambda x : x**2,range(1,n+1))))

"""I don't know if this is what you want. It uses reduce(operator.add,...) instead of sum, and it's in one line, but
I, at least, hate it."""
