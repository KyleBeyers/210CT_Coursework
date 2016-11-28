##210CT Labtask 1
##Task 2

##user input for number to test.
num = int( input("Enter a value: "))

def factorial(n):
    """function to calculate the factorial of a number using recursion"""
    if n == 0:
        return(1)
    else:
        ans = n*factorial(n-1)
        return(ans)

def trailingZeros(x):
    """Function to take the factorial answer, convert to string and count the zeros."""
    a = str(factorial(num))
    count = 0
    x = 1 ##starting value so the string can be counted from -1.
    for i in a:
        if a[-x] == "0":
            count = count + 1 ##everytime a zero is found count goes up.
            x = x + 1 ##changes value of x so that value before can be looked at.
    if count == 1:
        print("There is " + str(count) + " zero in the factorial of " + str(num))
    if count > 1:
        print("There are " + str(count) + " zeros in the factorial of " + str(num))
    if count == 0:
        print("There are no zeros in the factorial of " + str(num))

##Call to the function trailingZeros.
trailingZeros(num)
