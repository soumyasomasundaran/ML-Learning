#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 07:26:54 2018

@author: soumya

A numpy array is a grid of values, all of the same type, and is indexed by a tuple 
of nonnegative integers. Rank of the array is the dimension of the array; 
"""

import numpy as np
arr=np.array([0,2,37,8])#A list is converted to array
print (type(arr))
print ("Array is ",arr)

print (arr.shape)#prints dimension of array
for i in range(len(arr)):#printing Elements of the array
    print (arr[i])
arr[1]=90
print (arr)

