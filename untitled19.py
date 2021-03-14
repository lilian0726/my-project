# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:22:26 2021

@author: User
"""

age = input('Hello,enter your age.')

if float(age) >= 18 :
    print('adult')
else :
    print('not adult')
    
str1 = 'My name is '
str2 = 'Paul.'

str2 += 'str3'

print(str2 is str1)
print(str1)

result = str2.split(',')
print(result)

result_back = ' '.join(result)
print(result_back)