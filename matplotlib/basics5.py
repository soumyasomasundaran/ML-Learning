#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 22:41:16 2018

@author: soumya
"""
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(5)
# assume there are 5 students
y = (20, 35, 30, 35, 27) # their test scores
plt.bar(x,y)
# Bar plot
plt.show()
# Try commenting this an run
plt.scatter(x,y)
# scatter plot
plt.show()



import pandas as pd
df=pd.read_csv('FuelConsumption.csv')
df.hist()# Histogram
df.plot()
# Line Graph
df.boxplot()
# Box plot
