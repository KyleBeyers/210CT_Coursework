##210CT LabWeek 2
##Task 1

def perfectSquare(n):
    """Function to check if a value is a perfect square, or find the closest
    perfect square value to input"""
    
    x = 0 ##x is a variable used to find the square root of the input.
    if n > 0: ##make sure input is positive.
        while (x * x) < n:
            x = x + 1
            ##if x*x doesn't = input then keep increasing until it does,
            ##or until it becomes greater than input.

        if (x * x) != n:
            perfectSquare(n-1)
            ##if value isn't square number, use recursion to test next value down.

        if (x * x) == n:
            ##if value is perfect square, check if it was input or a number
            ##below the input.
            if n == value:
                print(str(n) + " is a perfect square.")
            else:
                print("Closest perfect square value is " + str(n))
    else:
        print("Value is not a positive integer!")
        
value = int( input("Please input positive value: "))
perfectSquare(value)
