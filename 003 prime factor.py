"""
What is the largest prime factor of the number 600851475143
"""
lar_prime=0
n=600851475143

def prime_check(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(int(n**0.5), 2, -1): 
    if n % i == 0 and prime_check(i):
        lar_prime = i
        break

print("the largest prime factor of the number 600851475143 is", lar_prime)