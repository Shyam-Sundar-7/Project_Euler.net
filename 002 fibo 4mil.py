"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

a=1
b=2
s=0
while(b<4_000_000):
    if b%2==0:
        s=s+b
    c=a+b
    a=b
    b=c

print("the sum of the even-valued terms is",s)