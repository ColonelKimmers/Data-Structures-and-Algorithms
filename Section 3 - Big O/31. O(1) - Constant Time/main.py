#import time

#CONST_NEMO = ["nemo"]

#CONST_EVERYONE = ["dory", "bruce", "marlin", "nemo", "gill", "bloat", "nigel", "squirt", "darla", "hank"]

#CONST_LARGE = ["nemo" for i in range(100000)]

#def findNemo(array):
#    for x in array:
#        if x == "nemo":
#            print("Found Nemo!")

#findNemo(CONST_LARGE)

CONST_BOXES = [0, 1, 2, 3, 4, 5]

def logFirstTwoBoxes(boxes):
    print(boxes[0])
    print(boxes[1])

logFirstTwoBoxes(CONST_BOXES)