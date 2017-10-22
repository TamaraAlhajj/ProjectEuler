""" Tamara Alhajj
    Project Euler Q5
    What is the smallest positive number that is divisible by all of the numbers from 1 to 20?
"""

checkList = [11, 13, 14, 16, 17, 18, 19, 20]


for num in range(2520, 999999999, 20): #start loop at 2520, smallest divisible num by 1-10
    if all(num%i == 0 for i in checkList): 
        print(num)
        break