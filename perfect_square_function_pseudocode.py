##210CT LabTasks 2
##Task 1 pseudocode

PERFECT_SQUARE(N):
    x <- 0
    if n > 0 then:
        while x * x < n:
            x <- x + 1
        if x * x != n then:
            PERFECT_SQUARE(N-1)
        if x * x = n then:
            if n = value then:
                output n is a perfect square
            if n < value then:
                output closest perfect square is n
    else:
        output value is not a positive integer

value <- user input converted to type int
PERFECT_SQUARE(value)
