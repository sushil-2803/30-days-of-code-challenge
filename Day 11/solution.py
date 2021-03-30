import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    sum = 0
    harr = []
    
    for l in range(0,4):
        for k in range(0,4):
            for i in range(l,l+3):
                for j in range(k,k+3):
                    if i == l+1 and ( j == k or j == k+2):
                        continue
                    else:
                        sum += arr[i][j]
            harr.append(sum)
            sum = 0
    
    print(max(harr))
