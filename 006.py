"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

n=100

sum_of_squares=n*(n+1)*(2*n+1)/6
squares_of_sum=n*(n+1)/2

print("the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is",int(squares_of_sum**2-sum_of_squares))