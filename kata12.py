""" 
Kata 12

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0] 
"""

def move_zeros(array):
    zeros=array.count(0)
    clean=[]
    for i in array:
        if i!=0:
            clean.append(i)
    for i in range (1,zeros+1):
        clean.append(0)
    return clean