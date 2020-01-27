#!/bin/python3
# link: https://www.hackerrank.com/challenges/ctci-array-left-rotation
import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    '''
    new array is split into 3 parts
    1. first element is the dth element of array a
    2. remainder is from dth element of a to end in array a
    3. last part is from index 1 to dth element of a
    '''
    output_array = [0 for i in range(len(a))]
    output_array[0] = a[d] # 1st element
    remainder = len(a)-d
    if remainder != 1:
        # remainder term
        output_array[1:remainder-1]=a[d+1:]
        output_array[remainder:]=a[0:d]
    else:
        # no remainder
        output_array[1:]=a[0:d]
    return output_array


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
