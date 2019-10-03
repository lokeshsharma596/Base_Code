#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    s,l,c=5,2,2
    if n==1:
        return 2
    else:
        for i in range(2,n+1):
            s=s//2*3
            l=s//2
            c=l+c
        return c



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

