#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min,max=0,0
    arr.sort()
    
    for i in range(len(arr)-1):
        min=min+arr[i]
    for j in range(1,len(arr)):
        max=max+arr[j]
    print(min,max)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

