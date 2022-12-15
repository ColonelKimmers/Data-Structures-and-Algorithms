import time

CONST_NEMO = ["nemo"]

CONST_EVERYONE = ["dory", "bruce", "marlin", "nemo", "gill", "bloat", "nigel", "squirt", "darla", "hank"]

CONST_LARGE = ["nemo" for i in range(100000)]

def findNemo(array):
    t0 = time.time()
    for x in array:
        if x == "nemo":
            print("Found Nemo!")
    t1 = time.time()

    print("Call to find Nemo took", t1-t0, "milliseconds")

findNemo(CONST_LARGE)