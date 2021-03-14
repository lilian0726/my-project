# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 18:11:30 2021

@author: User
"""

f = open("test_0.txt", "w")
f.write("0.2 0.9 0.8\n 1.0 0.1 0.2\n 0.5 0.7 0.8")
f.close()

f = open("test_0.txt", "r")
for line in f.readlines():
    print(line)
f.close

f = open("test_0.txt", "r")
for line in f.readlines():
    print(line.split(' ')[1])
f.close