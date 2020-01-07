#!/bin/python3
# link: https://www.hackerrank.com/challenges/counting-valleys/
import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    num_valleys = 0
    current_level = 0
    for num_steps in s:
        if num_steps == 'U':
            current_level += 1
        if num_steps == 'D':
            current_level += -1
        elif current_level==0:
            num_valleys += 1
    return num_valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
