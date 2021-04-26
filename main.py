# coding:utf-8

import sys
import math
import time
#import numpy as np
import collections
from collections import deque
from collections import Counter
import queue
import copy
import bisect #二分探索
import heapq
import itertools


#sys.setrecursionlimit(10**7)
#N, Q = map(int, input().split())
#G = [list(input()) for i in range(H)]
#A = list(map(int, input().split()))
#AB = [list(map(int, input().split())) for _ in range(K)]
#CW = [list(map(int, list(input()))) for _ in range(H)]
#li = sorted(li, reverse=True, key=lambda x: x[1])

R, X, Y = map(int, input().split())
ans = 0
You = math.sqrt(X**2 + Y**2)

if(You<R):
  print(2)
elif(You%R != 0):
  print(math.ceil(You/R))
else:
  print(int(You//R))
