def booooo(n):
    for i in range(len(n)):
        print("booooooo!")

booooo([1, 2, 3, 4, 5]) # Space complexity of O(1)

def arrayOfHiNTimes(n):
    hiArray = []
    for i in range(n):
        hiArray.append("hi")

    return hiArray

print(arrayOfHiNTimes(7)) # Space complexity of O(n)