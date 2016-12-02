##210CT LabTasks 3
##Task 3 - pseudocode

word <-- user input

def VOEWLREMOVER(s):
    if s = "" then:
        output s
    else:
        new_str <-- s without first letter
        first_let <-- first letter in s
        if first_let is a vowel then:
            output VOWELREMOVER(new_str)
        else:
            output first_let + VOWELREMOVER(new_str)

output VOWELREMOVER(word)
