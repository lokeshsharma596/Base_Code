#!/bin/python3

import os
import sys

def timeConversion(s):
    a,b=((s[0:2]),s[-2:])

    if b=='AM' and a=='12':
        a='00'
    elif b=='PM' and 1<=int(a)<=11:
        a=str(int(a)+12)

    return a+s[2:8]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

