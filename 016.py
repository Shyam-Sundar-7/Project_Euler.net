"""
What is the sum of the digits of the number 2^1000?
"""

n=2**1000
print(n)

def sum_of_digits(n):
    return sum(int(i) for i in str(n))

print(sum_of_digits(n))
