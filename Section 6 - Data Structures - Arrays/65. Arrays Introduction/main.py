CONST_STRINGS = ['a', 'b', 'c', 'd']
# 4x4 = 16 bytes of storage

print(CONST_STRINGS)

# Lookup

# print(CONST_STRINGS[2]) # O(1)

# Push - adds to end of list/array
CONST_STRINGS.append('e') # O(1)

print("Add E", CONST_STRINGS)

# Pop - removes from end of list/array
CONST_STRINGS.pop() # O(1)

print("Remove E", CONST_STRINGS)

# Unshift - Usually used to put an item at begging of an array - python lists doesnt have that (we use deque and appendleft instead)
CONST_STRINGS.insert(0, 'x') # O(n)

print("Insert X to beginning", CONST_STRINGS)

# Splice - does not exist in python, instead you slice with this syntax
CONST_STRINGS[2:0] = "Alien" # O(n)

print("Slice from C, insert 'Alien'", CONST_STRINGS)