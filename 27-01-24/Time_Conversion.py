#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import datetime as dt

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    t12=dt.strptime(s, '%I:%M:%S%p')
    t24= t12.strftime('%H:%M:%S')
    return t24

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
