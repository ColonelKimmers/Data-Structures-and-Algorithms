import time

CONST_NEMO = ["nemo"]

CONST_EVERYONE = ["dory", "bruce", "marlin", "nemo", "gill", "bloat", "nigel", "squirt", "darla", "hank"]

CONST_LARGE = ["nemo" for i in range(100000)]

def findNemo(array):
    for x in array:
        print("Running")
        if x == "nemo":
            print("Found Nemo!")
            break

findNemo(CONST_EVERYONE)