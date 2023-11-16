rank=1

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

i=2
while(rank<=10001):
    if is_prime(i):
        print(f"{rank} : {i}")
        rank+=1
    i+=1

