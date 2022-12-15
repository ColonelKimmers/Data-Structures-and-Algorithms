# What is the Big O of the function below? (Hint: you may want to go line by line)

def anotherfunChallenge(input):
    a = 5                       # O(1) runs once
    b = 10                      # O(1) runs once
    c = 50                      # O(1) runs once

    for i in input:             # O(n) runs for amount of elements in input
        x = i + 1               # O(n) runs for amount of elements in input
        y = i + 2               # O(n) runs for amount of elements in input
        z = i + 3               # O(n) runs for amount of elements in input

    for j in input:             # O(n) runs for amount of elements in input
        p = j * 2               # O(n) runs for amount of elements in input
        q = j * 2               # O(n) runs for amount of elements in input

    whoAmI = "I don't know"     # O(1) runs once

    # There are four O(1) and seven O(n)
    # 4 + n + n + n + n + n + n + n
    # Simplify to 4 + 7n
    # Big O is O(4 + 7n)
    # Simplify to O(n)