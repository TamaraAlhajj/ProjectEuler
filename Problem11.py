"""
Tamara Alhajj
Project Euler Q11
Find greatest product of four adjacent numbers in the 20×20 grid.
Diagonals included.
"""
from functools import reduce

def greatestProduct(grid, adj):
    """greatest product of adjacent numbers in the grid"""
    #assume all positive numbers in grid
    dimentions = (len(grid), len(grid[0]))
    multiplier = lambda x, y: x*y

    maxProduct = -1

    #horizontal and vertical
    for i in range(dimentions[0]): #rows
        for j in range(dimentions[1] - adj + 1): #col
            product = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
            if product > maxProduct:
                maxProduct = product
            product = grid[j][i] * grid[j+1][i] * grid[j+2][i] * grid[j+3][i]
            if product > maxProduct:
                maxProduct = product

    #both diagonals
    for i in range(dimentions[0] - adj):
        for j in range(dimentions[1] - adj + 1):

            product = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
            if product > maxProduct:
                maxProduct = product
            #reverse
            product = grid[i][j+3] * grid[i+1][j+2] * grid[i+2][j+1] * grid[i+3][j]
            if product > maxProduct:
                maxProduct = product

    return maxProduct

with open("grid.txt") as grid:
    numbers = [line.split() for line in grid]
    numbers = [[int(y) for y in x] for x in numbers]

print(greatestProduct(numbers, 4))