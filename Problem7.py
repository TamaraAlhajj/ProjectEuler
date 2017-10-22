""" Tamara Alhajj
	ProjectEuler Q7
	What is the 10 001st prime number?
"""

def isPrime(x):
	#assume x > 1
    n = x//2 
    for i in range(2, n+1):
	    if(x % i == 0):
		    return False
    return True

def nthPrime(n):
	prime = 2
	count = 1
	i = 3
	while count < n:
		if isPrime(i): 
			prime = i
			count += 1
		#do not check even numbers
		i += 2 
	return prime

print(nthPrime(10001))
