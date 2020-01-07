#!/bin/python3
# link: https://www.hackerrank.com/challenges/sock-merchant/problem
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    unique_nums = list(set(ar))
    total_pairs = 0
    for num in unique_nums:
        total_pairs += ar.count(num) // 2
    return total_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
