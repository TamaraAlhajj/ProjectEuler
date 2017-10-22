""" Tamara Alhajj
    Project Euler Q1
"""
def sum_Of_All_Multiples(a, b, bound):
    """Find the sum of all the multiples of a or b below bound."""
    sumOfMultiples = 0
    for i in range(0, bound):
        if (i%a == 0) or (i%b == 0):
            sumOfMultiples = sumOfMultiples + i
    return sumOfMultiples

#answer    
print(sum_Of_All_Multiples(3, 5, 1000))
