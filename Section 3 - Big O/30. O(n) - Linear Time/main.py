import time

CONST_NEMO = ["nemo"]

CONST_EVERYONE = ["dory", "bruce", "marlin", "nemo", "gill", "bloat", "nigel", "squirt", "darla", "hank"]

CONST_LARGE = ["nemo" for i in range(100000)]

def findNemo(array):
    for x in array:
        if x == "nemo":
            print("Found Nemo!")

findNemo(CONST_LARGE)