""" Tamara Alhajj
    Project Euler Q2
    By considering the terms in the Fibonacci sequence (starting at 1,2)
    whose values do not exceed four million,
    find the sum of the even-valued terms.
"""

#base case
p2 = 1
p1 = 2
Fibonacci = p1 + p2
sumOfEvens = 2

while Fibonacci < 4000000:
    temp = p1
    p1 = Fibonacci
    p2 = temp
    Fibonacci = p1 + p2 #next fib num in sequence
    if Fibonacci%2 == 0:
        sumOfEvens = sumOfEvens + Fibonacci

#answer
print(sumOfEvens)
