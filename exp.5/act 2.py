# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:35:36 2026

@author: ADMIN
"""

items = ["apple", "banana", "apple", "orange", "banana", "apple"]

frequency = {}

for item in items:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print(frequency)