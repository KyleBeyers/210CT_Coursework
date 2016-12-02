##210CT LabTasks 3
##Task 1 pseudocode.

string <-- "Reverse this string"
output string
newList <-- emptyList[]

def SPLITSTRING(s):
    word <-- ""
    for each character in string:
        if character = " " and word != "":
            add word to newList
            word <-- ""
        else:
            word <-- word + character
    if word != "":
        add word to newList
    output newList

def REV(l):
    if length of l = 0:
        output empty list
    else:
        output last character in l + REV(rest of the characters)


SPLITSTRING(string)
revList <-- REV(newList)
reversedWord <-- join revList
output reversedWord
    
