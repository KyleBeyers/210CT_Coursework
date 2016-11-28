##210CT LabTasks 3
##Task 1

##string <-- "Reverse this string"
##output string
##newList <-- emptyList[]
##
##def SPLITSTRING(s):
##    word <-- ""
##    for each character in string:
##        if character = " " and word != "":
##            add word to newList
##            word <-- ""
##        else:
##            word <-- word + character
##    if word != "":
##        add word to newList
##    output newList
##
##def REV(l):
##    if length of l = 0:
##        output empty list
##    else:
##        output last character in l + REV(rest of the characters)
##
##
##SPLITSTRING(string)
##revList <-- REV(newList)
##reversedWord <-- join revList
##output reversedWord

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
