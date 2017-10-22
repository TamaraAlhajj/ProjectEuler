""" Tamara Alhajj
    Project Euler Q3
    What is the largest prime factor of the number 600851475143 ?
"""

import math

def isPrime(n):
    for i in range (3,int(n**0.5),2):
        if n%i == 0:
            return False
    return True

def largestPrime(n):
    
    # Note: if we check upto num, runtime will be vary long
    # we know a number is prime if there are no prime factors < it's sqrt
    # because if there is a prime > the sqrt there MUST be one < sqrt
    # so you only need to check upto the root of n
    
    answer = 0
    for i in range(int(math.sqrt(n)),2,-1): 
        if (n%i == 0) and (isPrime(i)): 
            answer = i 
            break
    return answer

print(largestPrime(600851475143))  