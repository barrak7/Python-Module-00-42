#!/bin/python

import sys
import string

l = len(sys.argv)
if (l != 3) or (sys.argv[1].isnumeric() == True) or (sys.argv[2].isnumeric() == False):
    print("Error")
    sys.exit()
ls = sys.argv[1].split()
def nop(s):
    p = string.punctuation
    n = 0
    for c in s:
        if c in p:
            n = n + 1
    return n
ls = [i for i in ls if len(i) - nop(i) > int(sys.argv[2])]
print(ls)
n = 0
for i in ls:
    ls[n] = i.translate(str.maketrans('','', string.punctuation))
    n = n + 1
print(ls)
