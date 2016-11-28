##210CT Week 1 Labsheet
##Task 1

##import random
import random

numList = [5,3,8,6,1,9,2,7]

def shuffle(l):
    """Function to manually shuffle array using randint for index"""
    newList = [] ##empty list to be filled with random values from original.
    index = list(range(0,len(numList)))##list of indices from numList
    random.shuffle(index) ##randomly shuffle the indices.
    for i in index:
        ##for loop to go through list of shuffled indices and pull random value from original list.
        a = numList[i]
        newList.append(a)
    print(newList)

##call to the function.
shuffle(numList)

