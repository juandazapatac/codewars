""" 
Kata5 

This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z. 
"""

def accum(s):
    count=0
    for i in s:
        count+=1
        i_up=i.upper()
        i_low=i.lower()
        if count==1:
            o=i_up
        else:
            o=o+"-"+i_up+i_low*(count-1)
    return o