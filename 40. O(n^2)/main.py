# Log all pairs of array
CONST_BOXES = ["a", "b", "c", "d", "e"]

def logAllPairsOfArray(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i], array[j])

logAllPairsOfArray(CONST_BOXES)

# Nested for-loops become multiplication
# This is O(n * n)
# Simplify to O(n^2)