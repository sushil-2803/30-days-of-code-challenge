#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
swap=0
# Write Your Code Here
for i in range(len(a)-1):
    for j in range(0,n-i-1):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
            swap+=1

print(f"Array is sorted in {swap} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")