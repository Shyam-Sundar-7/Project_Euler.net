"""
Find the sum of all the primes below two million.
"""
from rich.progress import track
from tqdm import tqdm
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

primes = []
for i in track(range(2,2_000_000)):
    if is_prime(i):
        primes.append(i)

print(sum(primes))


