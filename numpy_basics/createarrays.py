#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 07:43:15 2018

@author: soumya
"""

#create a 2D array
import numpy as np
arr1 = np.array([[0,1,2],[3,4,5]])
print ("Dimension of the array", arr1.shape)
print ("Elements of the 2D array",arr1)
#printing elements randomly
print (arr1[0, 0], arr1[0, 1], arr1[1, 0])


#creating arrays 

a = np.zeros((3,3))
print ("Inital array",a)

b = np.ones((2,2))
print (b)

#constant values
c = np.full((3,2),9)
print (c)

#random Elements
d = np.random.random((3,3))
print (d)

e = np.eye(4)
print (e)

