"""
Tamara Alhajj
ProjectEuler Q9
A Pythagorean triplet:  a < b < c, for which, a^2 + b^2 = c^2
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
def triples(t):
    #if triple: (a+b+c)^2 = t^2
    #expand: a^2 + b^2 + c^2 + 2ab + 2ac + 2bc = t^2
    #by pythagoras and factor 2: c^2 + ab + ac + bc = t^2 /2
    #c(a + b + c) + ab
    #thus given a + b + c = t: ab + tc = t^2 / 2
    check = (t**2)/2 
    for a in range(1, t):
        for b in range(a, t - a):
            c = t - a - b  #from given a + b + c = t
            if a * b + t * c == check: return(a*b*c)
#answer
print(triples(1000))