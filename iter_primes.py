import itertools
from math import factorial


def primes():
    """Compute and generate prime numbers in a given interval"""
    n = 1
    while True:
        n += 1
        if (factorial(n - 1) + 1) % n == 0:  #  Wilson's theorem 
            yield n

num = int(input('To set Interval input a positive integer number: '))
print('List of prime numbers in the given interval is: ', \
      list(itertools.takewhile(lambda x : x <= num, primes())))
