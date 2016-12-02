##210CT LabTasks 5
##Task 1

intList = [1,2,3,4,1,5,1,6,7]
newList = [] #list to store sublists

def subList(L):
    '''function to split a list of integers into sublists of asc order'''
    if L == []:
        #if the list is empty it is returned
        return L
    else:
        start = 0 #start index for slicing
        for index in range(len(L)-1):
            if L[index] > L[index+1]:
                #if first value is bigger than second (not asc) then add values
                #between start and index + 1 to new list
                newList.append(L[start:index+1])
                start = index + 1
        newList.append(L[start:]) #add remaining values into new list 

def subSeqMax(newL):
    '''function to find the largest sublist and return it.'''
    maxList = 0 #variable to store largest sublist
    maxLength = 0 #variable to store length of largest sublist
    for index in range(len(newL)-1):
        if len(newL[index]) > maxLength:
            #value bigger than current max is stored, along with its
            #corrosponding sublist
            maxLength = len(newL[index])
            maxList = newL[index]
    print(maxList)
    
subList(intList)
subSeqMax(newList)
