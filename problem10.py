#project euler problem 10
from NumberTests import isPrime
from NumberTests import getFactors


def main():
    number = 2000000
    factors = getFactors(number)
    print(factors)

    for f in factors:
        if isPrime(f):
            print(f)
    prime_sum = 0
    for f in factors:
        if isPrime(f):
            prime_sum += f
    print(prime_sum)
