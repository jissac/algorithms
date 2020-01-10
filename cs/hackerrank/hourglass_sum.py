#!/bin/python3
#link: https://www.hackerrank.com/challenges/2d-array/
import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    num_rows = len(arr)
    num_cols = len(arr[0])
    max_arr_val = []
    for i in range(1,num_rows-1):
        for j in range(1,num_cols-1):
            print(arr[i][j])
            arr_sum = (arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]) \
                        + (arr[i][j]) \
                        + (arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1]) 
            max_arr_val.append(arr_sum)
    #print(max_arr_val)
    return max(max_arr_val)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
