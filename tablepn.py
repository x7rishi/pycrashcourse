#!/usr/bin/python3
# tablepn.py - print the table in matrix form 
"""
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']]

output - 
    apples Alice dogs
    oranges Bob cats
    cherries Carol moose
    banana David goose
"""

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]


maxl = len(max(tableData))
for i in range(len(tableData)):
    for j in range(len(tableData[i])) :


