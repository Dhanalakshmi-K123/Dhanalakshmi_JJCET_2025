#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    strlen = len(s)
    if strlen == 0 or strlen%2 != 0:
        return -1

    tochange = 0
    sublen = strlen//2
    lhs, rhs = s[:sublen], list(s[sublen:])
    for char in lhs:
        if char not in rhs:
            tochange += 1
        else:
            rhs.remove(char)
    return tochange
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
