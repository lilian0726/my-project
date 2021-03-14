# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 20:26:06 2021

@author: User
"""

import matplotlib.pyplot as plt # import matplotlib
import numpy as np          # import numpy
x = np.linspace(0, 10, 100)
y = np.cos(x)
z = np.sin(x)
plt.plot(x, y, label='Cos')
#plt.show()
plt.plot(x, z, label='Sin')
plt.legend(loc = 'upper right')
plt.show()