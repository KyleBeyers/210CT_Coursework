##210CT LabTask 3
##Task 2 pseudocode

num <-- user input

def PRIME(x,y):
    if x < 2 then:
        output x is not a prime
    if y = 1 then:
        output x is a prime
    else:
        if x % y = 0 then:
            output x is not a prime
        else:
            output PRIME(x,y - 1)

def PRIMECHECK(n):
    if n > 1 then:
        PRIME(n, n - 1)
    else:
        output n is not a prime

PRIMECHECK(num)
