# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 13:15:56 2021

@author: betty
"""

i = (int(input("請輸入星星塔層數:")))
for y in range(i):
    print("*" * (y + 1))
for y in range(i-1,0,-1):
    print("*" * y)