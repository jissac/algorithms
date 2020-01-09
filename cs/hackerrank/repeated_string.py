#!/bin/python3
#link: https://www.hackerrank.com/challenges/repeated-string/
import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    ## Memory inefficient ##
    # repeated = s*((n//len(s))+1)
    # repeated = repeated[:n]
    # num_a = repeated.count('a')

    ## More efficient way
    num_a_init = s.count('a')
    repeated_count = n//len(s)
    remainder = n%len(s)
    remainder_slice = s[:remainder].count('a')
    num_a = num_a_init * repeated_count + remainder_slice
    return num_a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
