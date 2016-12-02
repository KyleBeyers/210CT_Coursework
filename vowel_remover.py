##210CT LabTasks 3
##Task 3

word = input("Enter a word: ")

def vowelRemover(s):
    if s == "":
        #if string is empty it is returned.
        return s
    else:
        new_str = s[1:len(s)]
        first_let = s[0]
        #first letter is seperated from the string.
        #remaining letters stored in new_str.
        if first_let in "aeiouAEIOU":
            #first letter checked; if it is a vowel new_str returned
            #without first letter which is vowel.
            return vowelRemover(new_str)
        else:
            #if first leter isn't vowel, it is stored to be added back.
            return first_let + vowelRemover(new_str)

print(vowelRemover(word))
