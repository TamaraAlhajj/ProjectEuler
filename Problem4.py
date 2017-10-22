""" Tamara Alhajj 
    Project Euler Q4
    Find the largest palindrome made from the product of two 3-digit numbers.
"""

def palindrome(num):
    forward = str(num)
    backward = str(num)[::-1]
    if (forward == backward):
        return True
    else:
        return False

def largestPalindrome(d):
    top = (10**d)-1
    bottom = 10**(d-1)
    answer = 0
    for i in range(top, bottom, -1):
        for j in range(top, bottom, -1):
            if ((palindrome(i*j)) & (i*j > answer)):
                answer = i*j
    return answer

print(largestPalindrome(3))