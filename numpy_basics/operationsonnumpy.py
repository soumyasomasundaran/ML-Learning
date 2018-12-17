#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 07:45:08 2018

@author: soumya
"""
import numpy as np
g = np.arange(10)#creates array of regularly incrementing values
print (g)

h = np.array([[0,1,2.0],[0,0,0],(1,3.,2.)])#mix of tuple and list
print (h)

i = np.arange(1, 8, dtype=np.float)
print (i)
j = np.linspace(2., 4.,9)#creates items spaced equally between the specified beginning and end values
print (j)
print ("Indices")
k = np.indices((3,2))

'''The output shape is obtained by prepending the number of dimensions in front of the tuple of dimensions, i.e. if dimensions is a tuple (r0, ..., rN-1) of length N, the output shape is (N,r0,...,rN-1).

The subarrays grid[k] contains the N-D array of indices along the k-th axis. Explicitly:

grid[k,i0,i1,...,iN-1] = ik
'''
print ("Dimension is ",k.shape)
print (k)