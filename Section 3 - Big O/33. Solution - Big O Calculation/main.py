def funChallenge(input):
    a = 10                      #O(1) runs once
    a = 50 + 3                  #O(1) runs once

    for i in len(input):        #O(n) n = length of input
        #anotherFunction()      #O(n) assuming no other loop is within this function
        stranger = True         #O(n) called by the amount of length of input
        a += 1                  #O(n) called by the amount of length of input

    return a                    #O(1) runs once
    
    #There are three O(1) and four O(n)
    #3 + n + n + n + n
    #Simplify to 3 + 4n
    #Big O is O(3 + 4n)
    #Simplify to O(n)

funChallenge()