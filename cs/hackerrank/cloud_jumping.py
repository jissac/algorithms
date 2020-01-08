#!/bin/python3
#link: https://www.hackerrank.com/challenges/jumping-on-the-clouds
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    min_jumps = 0
    cur_pos = 0
    max_idx = len(c)-1
    for i,clouds in enumerate(c):
        #print( i,clouds)
        if cur_pos+2 < max_idx:
            if c[cur_pos+2] != 1:
                cur_pos += 2
            else:
                cur_pos += 1
            min_jumps += 1
    min_jumps +=1
    return min_jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
