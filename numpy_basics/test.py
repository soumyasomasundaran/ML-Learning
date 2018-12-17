#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 20:34:45 2018

@author: soumya
Read more about indexing @:
https://docs.scipy.org/doc/numpy-1.13.0/user/basics.rec.html
"""
import numpy as np
x = np.zeros((2,2), dtype=[('a', np.int32), ('b', np.float64, (2,2))])
print (x['a'].shape)
print (x['a'].dtype)
print (x[0])
print (x['b'].shape)
print (x[1])
#print (x)

