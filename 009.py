"""
A Pythagorean triplet is a set of three natural numbers, 
a,b,c, for which, a2 + b2 = c2

For example, 3**2+4**2+=9+16=25

There exists exactly one Pythagorean triplet for which 
a+b+c=1000.
Find the product a*b*c 
."""

def is_pythagoras(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False
    

for c in range(1,1000):
    for b in range(1,c):
        a=1000-b-c
        if is_pythagoras(a,b,c):
                print(a*b*c)
                exit()