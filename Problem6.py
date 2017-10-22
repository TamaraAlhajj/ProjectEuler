""" Tamara Alhajj
	Project Euler Q6 
	Find the difference between 
	the sum of the squares  
	and the square of the sum
	of the first one hundred natural numbers
"""

sumOfSquares = 0
for i in range(1,101):
	square = i*i
	sumOfSquares += square

sumOfAll = 0
for j in range(1,101):
	sumOfAll += j

squareOfSum = sumOfAll*sumOfAll

solution = squareOfSum - sumOfSquares

print(solution)