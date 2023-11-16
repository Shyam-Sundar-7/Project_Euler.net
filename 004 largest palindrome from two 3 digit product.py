"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""
from rich.progress import track

def is_palindrome(n):
    return str(n) == str(n)[::-1]

max=0
for i in track(range(100,1000)):
    for j in range(100,1000):
        if i*j>max and is_palindrome(i*j):
            max=i*j

print("the largest palindrome is",max)
            
