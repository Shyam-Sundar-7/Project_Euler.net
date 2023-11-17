"""
1000-digit Fibonacci Number
"""

def fib(n):
    fib = [0] * (n + 1)
    fib[1] = 1
    fib[2]=1
    # Calculate Fibonacci numbers from 2 to n
    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]




n=12
while(len(str(fib(n))) < 1000):
    n+=1
print(n)
print(fib(n))
