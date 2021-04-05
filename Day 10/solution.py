#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binar=bin(n)[2:]
    b=str(binar)
    s=b.split('0')
    res = max(s, key = len)
    print(len(res))
