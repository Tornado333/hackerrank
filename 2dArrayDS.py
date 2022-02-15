
import math
import os
import random
import re
import sys

# problem : https://www.hackerrank.com/challenges/2d-array/problem


def hourglassSum(arr):
    newsum = []
    for i in range(4):
        for j in range(4):
            glass = sum(arr[j][i:i+3]) + arr[j+1][i+1] +  sum(arr[j+2][i:i+3])
            newsum.append(glass)
    return max(newsum)


'''
OLD SOLUTION :

def hourglassSum(arr):
    newsum = []
    new = []
    for i in range(4): #first row of glasses
        glass = sum(arr[0][i:i+3]) + arr[1][i+1] +  sum(arr[2][i:i+3])
        newsum.append(glass)
        
    for i in range(4): #second row of glasses
        glass = sum(arr[1][i:i+3]) + arr[2][i+1] +  sum(arr[3][i:i+3])
        newsum.append(glass)
    
    for i in range(4): #third row of glasses
        glass = sum(arr[2][i:i+3]) + arr[3][i+1] +  sum(arr[4][i:i+3])
        newsum.append(glass)
    
    for i in range(4): #fourth row of glasses
        glass = sum(arr[3][i:i+3]) + arr[4][i+1] +  sum(arr[5][i:i+3])
        newsum.append(glass)
    return max(newsum)
        
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
    '''
