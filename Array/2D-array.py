#https://www.hackerrank.com/challenges/2d-array/problem?h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    array=[]    
    for i in range(0,4):
        for j in range(0,4):
            top=arr[i][j]+arr[i][j+1]+arr[i][j+2]
            mid=arr[i+1][j+1]
            last=arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            sum_=top+mid+last
            array.append(sum_)
    return max(array)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
