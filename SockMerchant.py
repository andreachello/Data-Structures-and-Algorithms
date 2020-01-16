#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    x = {}
    for i in ar:
        if i not in x:
            x[i] = 0
        x[i] += 1
    print(x)
    count_pairs = 0
    for i in x:
        if x[i] % 2 == 0 and x[i] >= 2:
            count_pairs += x[i] // 2  
        elif x[i] % 2 != 0 and x[i] >= 2:
            count_pairs += (x[i]-1) // 2  
    return(count_pairs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
