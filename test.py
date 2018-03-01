# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 21:21:00 2018

@author: image
"""

import time 
from numba import jit

@jit
def testSum():
    s=0
    for k in range(1,1000000001):
        s+=k
    return s


t=time.clock()
s=testSum()
print t
print time.clock()-t
print (s)