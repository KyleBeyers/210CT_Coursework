##210CT LabTasks 3
##Task 2

num = int( input("Enter a positive integer: "))

def Prime(x,y):
    """Function to check if a number is a prime. This uses recursion to
    check if each number below x is divisible or not."""
    if x < 2:
        print(str(x) + " is not a prime number.")
        #lowest prime is 2, so anything below isn't a prime.
    if y == 1:
        print(str(x) + " is a prime number.")
        #when y reaches 1, that means only number divisible is 1 or x.
    else:
        if (x % y) == 0:
            print(str(x) + " is not a prime number.")
            #y isn't 1, so another value that produces no remainder means
            #another number is divisible.
        else:
            return Prime(x,y - 1) #check the next y down if not divisible.

def PrimeCheck(n):
    """Functon to prevent division of zero by checking if entered value is
    a 1."""
    if n > 1:
        Prime(n,n - 1)
        #runs the recursive funtion if value is greater than 1.
    else:
        print(str(n) + " is not a prime number.")
        #value <= 1 therefore cannot be prime.
        
PrimeCheck(num)
