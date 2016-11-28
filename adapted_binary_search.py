##210CT LabTasks 4
##Task 1

##L <- list of ints
##High <- user input integer
##Low <- user input integer
##
##DEF ADAPTED_BINARY_SEARCH(A,L,H):
##    startVal <- 0
##    endVal <- length of list - 1
##    valInRange <- False
##    while startVal <= endVal and valInRange <- False:
##        midVal <- (startVal + endVal)//2
##        if midVal of list is between l and h then:
##            valInRange <- True
##        else:
##            if midVal of list < l then:
##                startVal <- midVal + 1
##            elif midVal of list > h then:
##                endVal <- midVal - 1
##    return ValInRange
##output ADAPTED_BINARY_SEARCH(L,Low,High)

L = [2,3,5,7,9,13,15,20]
High = int( input("Enter high value for interval: "))
Low = int( input("Enter low value for interval: "))

def AdaptedBinarySearch(a,l,h):
    """Function to check if there are values within a given interval
    using binary search"""
    startVal = 0 #First element in list is index 0.
    endVal = len(a)-1 #Last element is length - 1.
    valInRange = False #value(s) not found yet so false.
    while startVal <= endVal and not valInRange:
        midVal = (startVal + endVal)//2
        if a[midVal] >= l and a[midVal] <= h:
            valInRange = True
            #if value is in interval variable changed to true.
        else:
            if a[midVal] < l:
                startVal = midVal + 1
                #if midpoint less than low value, midpoint and below
                #is removed
            elif a[midVal] > h:
                endVal = midVal - 1
                #if midpoint is higher than high value, midpoint and
                #onwards is removed

    return valInRange
                
print(AdaptedBinarySearch(L,Low,High))

##BigO of this algorithm is O(n).
