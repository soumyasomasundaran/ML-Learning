#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 22:48:45 2018

@author: soumya
"""
import matplotlib.pyplot as plt
import numpy as np
# generate sample data
x = np.linspace(0, 20, 1000)
y = np.sin(x)
#100 evenly-spaced values from 0 to 50
# customize axis labels
plt.plot(x, y, label = 'Sample Label')
plt.title('Sample Plot Title')
# chart title
plt.xlabel('x axis label')
# x axis title
plt.ylabel('y axis label')
# y axis title
plt.grid(True)
# show gridlines
# add footnote
plt.figtext(0.995, 0.01, 'Footnote', ha='right', va='bottom')
# add legend, location pick the best automatically
plt.legend(loc='best', framealpha=0.5, prop={'size':'small'})
# tight_layout() can take keyword arguments of pad, w_pad and h_pad.
# these control the extra padding around the figure border and between
#subplots
# The pads are specified in fraction of fontsize.
plt.tight_layout(pad=1)
# Saving chart to a file
plt.savefig('filename.png')
plt.close() # Close the current window to allow new plot creation on
#separate window / axis, alternatively we can use show()
plt.show()