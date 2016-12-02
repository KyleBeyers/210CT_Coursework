##210CT LabTasks 3
##Task 1

string = "Reverse this string"
print(string)
newList = []

def splitString(s):
    """function to split string words into individual items in list."""
    word = "" #variable to make the word so it can be put in new list.
    for s in string:
        if s == " " and word != "":
            #when both conditions are met this means a space is reached
            #and word has added up the characters to make the word.
            newList.append(word)
            word = "" #return to nothing for next word.
        else:
            word = word + s # adds character onto word.
    if word != "":
        #no space at end of string, so word added to new list
        newList.append(word)
    return(newList)

def rev(l):
    if len(l) == 0:
        return[] #if there is no contents in list empty list is returned.
    else:
        return [l[-1]] + rev(l[:-1]) #starts from back and works towards front.
    

splitString(string) #runs function to split string into list
revList = rev(newList) #reverses the list
reversedWord = ' '.join(revList) #joins the list back together into string
print(reversedWord)
