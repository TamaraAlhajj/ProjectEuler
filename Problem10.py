""" 
Tamara Alhajj
Project Euler Q10
Find the sum of all the primes below two million.

https://en.wikipedia.org/wiki/Sieve_of_Sundaram 
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
https://en.wikipedia.org/wiki/Wheel_factorization
https://en.wikipedia.org/wiki/Sieve_of_Atkin
"""
def sumOfAll(n):
    """ sum of all primes below bound n """
    sieve = [True] * n
    sieve[0], sieve[1] = [False]*2
    sieve[2] = True

    #iteratively marking composite
    for index, boolean in enumerate(sieve):
        if boolean:
            #set all multiples of num index to false
            #composites before square will already be marked
            sieve[index**2::index] = [False] * len(sieve[index**2::index])
    #add up primes
    sumOfPrimes = 2
    for num in range(3, n, 2):
        if sieve[num]: sumOfPrimes += num
    return sumOfPrimes

print(sumOfAll(2*10**6))