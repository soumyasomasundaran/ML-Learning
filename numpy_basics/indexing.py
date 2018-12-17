#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 08:22:00 2018

@author: soumya
"""

#Filed access


x = np.zeros((3,3), dtype=[('a', np.int32), ('b', np.float64, (3,3))])
print ("x['a'].shape: ",x['a'].shape)
print ("(x['a'].dtype: ", x['a'].dtype)
print ("x['b'].shape: ", x['b'].shape)
print ("x['b'].dtype: ", x['b'].dtype)
#Basic Slicing

x = np.array([5, 6, 7, 8, 9])
print (x[1:5:1]    )    
print (x[-2:5])
print (x[-1:1:-1])
'''
Negative k makes stepping go toward smaller indices. Negative i and j are
interpreted as n + i and n + j where n is the number of elements in the
corresponding dimension.'''
