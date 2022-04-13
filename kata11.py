""" 
Kata 11

Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  "" 
"""

def solution(s):
    s2=""
    for i in s:
        if i==i.upper():
            s2=s2+" "+i
        else:
            s2=s2+i
    return s2