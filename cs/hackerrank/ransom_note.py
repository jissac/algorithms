#!/bin/python3
# link: https://www.hackerrank.com/challenges/ctci-ransom-note
import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # print(magazine,note)
    mag_count = Counter(magazine)
    note_count = Counter(note)
    if len(note_count-mag_count) == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
