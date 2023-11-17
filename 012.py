"""
What is the value of the first triangle number to have over five hundred divisors?
"""


def triangle_number(n):
    return n * (n + 1) // 2 

def number_of_factors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2
    return count

n=1
while(number_of_factors(triangle_number(n)) < 500):
    n+=1

print(n)
print(triangle_number(n))