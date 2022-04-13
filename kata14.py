""" 
Kata 14

The main idea is to count all the occurring characters in a string. 
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}. """

def count(string):
    l=[]
    lc=[]
    dic={}
    for i in string:
        l.append(i)
    for j in string:
        if j not in lc:
            lc.append(j)
    for k in lc:
        v=l.count(k)
        dic[k]=(v)
    return dic