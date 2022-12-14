import math


def printFirstItemThenFirstHalfThenSayHi100Times(items):
    print(items[0])

    middleIndex = math.floor(len(items) / 2)
    index = 0

    while (index < middleIndex):
        print(items[index])
        index += 1

    for i in range(0, 100):
        print("hi")

# O(1 + n/2 + 100)
# Rule 2: Drop the constants
# O(n + 1)
# Simplified to O(n)

def compressBoxesTwice(boxes):
    for i in range(len(boxes)):
        print(boxes[i])

    for i in boxes:
        print(boxes[i])

# O(2n)
# Rule 2: Drop the constants
# O(n)