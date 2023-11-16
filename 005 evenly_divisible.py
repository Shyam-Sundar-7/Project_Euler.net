"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?
"""
import math
from rich.progress import track

small=math.factorial(20)
numbers=[i for i in range(1,21)]

def is_divisible(n):
    for i in numbers:
        if n%i!=0:
            return False
    return True

import time
start=time.time()
n=20
while(True):
    if is_divisible(n):
        print(n)
        break
    n=n+20
end=time.time()

print("time taken",end-start)

# num=0
# for i in track(range(20,small,20)):
#     if is_divisible(i):
#         num=i
#         break

# print(num)