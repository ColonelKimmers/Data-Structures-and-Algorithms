def printAllNumbersThenAllPairSums(numbers):
    
    print("these are the numbers:")
    for i in range(len(numbers)):           #O(n)
        print(numbers[i])

    print("and these are their sums:")
    for i in range(len(numbers)):           #O(n^2)
        for j in range(len(numbers)):
            print(numbers[i] + numbers[j])

printAllNumbersThenAllPairSums([1, 2, 3, 4, 5])

# O(n + n^2)
# Rule 4: Drop Non Dominant Terms
# O(n^2)

# Another example:
# O(x^2 + 3x + 100 + x/2)
# x^2 is most significant
# 100 is dominant, but in scale x^2 can become much larger
# So we simplify to O(x^2)