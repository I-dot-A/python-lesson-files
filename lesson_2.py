import time
"""SETS"""
# Mutable
# Unordered (the order is random)
# No indices

# Empty set
items = set()

# Not empty set
items = {2, 3, 4} # curly brackets

# Random order
items = {1, 2, "three", -1}
print(items)

# No duplicates
items = {1, 1, 2, 2, 2, 3}
print(items) # Should print just {1, 2, 3}

# Finding an item in a set is very fast
#nums_list = [i for i in range(10000000)]
#nums_set = {i for i in range(10000000)}
#start_time = time.time()
#if 9000000 in nums_list: print(f"List finding time: {time.time() - start_time}")
#start_time = time.time()
#if 9000000 in nums_set: print(f"Set finding time: {time.time() - start_time}")

# Methods
# .add() - adds an item to the set
items = {1, 2, 3, 4, 5}
print(items, "Before .add()")
items.add(6)
print(items, "After .add(6)")
items.add(1) # No duplicates
print(items, "Only one 1")

# .pop() - removes a random item from a set
items.pop()
print(items)

stuff = {"car", "banana", 2.3, 3, True}
stuff.pop()
print(stuff)
print()

# .remove and .discard - remove a specified item from a set
# .remove raises an error when the item is not found
# .discard does not raise an error if the item is not found
items = {1, 2, 3, 4, 5}
items.remove(5)
print(items, "5 is now gone after .remove(5)")
items.discard(5) # Does not cause an error
#items.remove(5) # This one does
items.discard(3)
print(items, "3 is now gone after .discard(3)")
print()

# .update (3 types)
nums_1 = {1, 2, 3, 4, 5}
nums_2 = {4, 5, 6, 7, 8}
# .update updates the first set by adding the second set (no duplicates added)
# You can't add sets with '+'
print(nums_1, "nums_1 Before .update()")
print(nums_2, "nums_2")
nums_1.update(nums_2)
print(nums_1, "nums_1 After .update()")
print(nums_2, "nums_2 is not updated")
print()

# .intersection_update()
# This method updates the first set by only
# including all common items between the 2 sets
nums_1 = {1, 2, 3, 4, 5}
print(nums_1, "nums_1 Before .intersection_update()")
print(nums_2, "nums_2")
nums_1.intersection_update(nums_2) # Should now be {4, 5}
print(nums_1, "nums_1 After .intersection_update()")
print()

# .difference_update()
# This method updates the first set by only
# keeping items that are in set_1 that are not in set_2
nums_1 = {1, 2, 3, 4, 5}
print(nums_1, "nums_1 Before .difference_update()")
print(nums_2, "nums_2")
nums_1.difference_update(nums_2) # Should now be {1, 2, 3}
print(nums_1, "nums_1 After .difference_update()")
print()

"""DICTIONARIES"""
# Mutable
# Ordered and indexed, but not 0-indexed
# Stores key:value pairs

# Empty dictionary (2 ways)
empty_dict = dict() # with dict()
empty_dict = {} # open-close curly brackets

# dictionary = {[key]: [value], [key2]: [value2]}
cookbook = {"Omelet": ("eggs", "cheese", "salt"), "Water": "water"}
dictionary = {"One": 1, "Two": 2, "Three": 3}
print(cookbook)
print()

# Keys must be immutable
dictionary = {1: 1, "Two": 2, (3, 4): True}
#dictionary = {[2, 1]: 1, "2": 2} # Causes an error since lists are mutable

# Dictionaries are ordered
dictionary = {"One": 1, "Two": 2, "Three": 3}
#print(dictionary[0]) # This doesn't work
print(dictionary["One"]) # To print at an index, specify the key
print()

# 2 ways to add a new key:value pair
# dict[new key] = new value
print(dictionary, "before")
dictionary["Four"] = 4
print(dictionary, "after")

# .update() - does the same thing, which is to add a new item if it's
# not already there, otherwise, update the specified key to the new value
dictionary.update({"Five": 5})
print(dictionary, "after .update()")

dictionary["One"] = 11
print(dictionary)
dictionary.update({"One": 1})
print(dictionary)

# More methods
# .pop(key) - removes a specified key:value pair, returns the value
dictionary.pop("Three")
print(dictionary, ".pop('Three')")
x = dictionary.pop("Four") # x = popped value
print(x)

# .popitem() - removes the last item from the dictionary
dictionary.popitem()
print(dictionary, "5 is gone")

print()

# .items() - returns the items in the dictionary as a list of tuples
print(dictionary.items())

# .keys() - returns a list of the dictionary keys
print(dictionary.keys())

# .values() - returns a list of the dictionary values
print(dictionary.values())

"""ALL 4 DATA TYPES (LISTS, TUPLES, SETS, DICTIONARIES)
CAN HOLD DIFFERENT VARIABLE TYPES INSIDE"""

list_stuff = [1, 2, True, "24", 2.5, [2, 3], (2, 3, "hello")]
tuple_stuff = ([1, 2, 3], False, "boi", 3, (2, 3))
set_stuff = {1, 2, (1, 3), 2.6} # Sets can only hold immutable types
dict_stuff = {3: "2", True: (True, False), (3, "boi"): [1, 2, {3, 4}, {3: 3}]}
print()
print()
print()
print()
print()


"""IF STATEMENTS"""
# General syntax: if [condition]: [code]
x = 2
if x == 2: # == tests for equality
    print("x = 2") # Python tells which code goes where based on indents
                   # An indent is usually 4 spaces, can also use tab

#if x == 2:
#print("x = 2") # Bad indent (syntax error)

# elif and else
if x == 1:
    print("x = 1")
elif x == 2: # else if
    print("x = 2")
else:
    print("idk")

if x == 0:
    pass # Placeholder keyword for unfinished code
elif x == 1:
    pass
elif x == 3: # You can include more than one elif statement
    print("x = 3")
else:
    print("x does not equal 1, 0, or 3")

print()

# ==/!=/is
# == checks for equality
# != checks for inequality
# is checks if they are the same object
print(x == 2)
print(x != 1)
print()

nums_1 = [2, 3, 4]
nums_2 = nums_1.copy() # Different, but equal list to nums_1
nums_3 = nums_1

print(nums_1 == nums_2) # True
print(nums_1 is nums_2) # False
print(nums_1 is nums_3) # True because they point to the same object 

print()

# Other examples of is

type_x = type(x) # Stores the type of x, which is int
if type_x == int:
    print("== works")

if type_x is int: # Likely the better option
    print("is works")

print()

# NoneType, Python's version of null
nothing = None # None basically means a value of nothing

if nothing == False: # None is not false
    print("nothing == False")
elif nothing is False:
    print("nothing is False")
elif nothing == 0: # None is not 0
    print("nothing is 0")
elif nothing: # Tests if it exists/is True/is not None
    print("nothing is True")
elif nothing is None: # Could use == None, but is None
    print("nothing is None")

print()

# and/or
# and tests if two things are true
# or tests if one or the other thing is true
x = 2
if x == 2 and x > 0:
    print("Success!")

if x == 2 or x > 100:
    print("Success!")

if x < 0 or x > 2 or type(x) is int:
    print("Success!")

# If you want a certain comparison to be made first, use parenthesis
if (type(x) is int and x == 2) or x < 1:
    print("Success!")

# not keyword
if not x == 1: # testing it the following is false instead of true
    print("Success!")

if not x == 2 or x < 0: # The part testing false returned true,
                        # and the part testing true returned false, so it fails.
    print("Success!")
else:
    print("Not success.")

if not (x == 2 or x < 0): # if x != 2 and x >= 0 --> False
    print("Success!")
else:
    print("Not success.")

print()

# Ternary if statements
word = "spaghetti"
# Let's make an if statement that tests if word is longer than 5 letters,
# otherwise, it'll print something else
if len(word) > 5:
    print("word > 5 letters")
else:
    print("word < 5 letters")

# We can do all this in 1 line

print("word > 5 letters") if len(word) > 5 else print("word < 5 letters")
# else version
print("word < 5 letters") if len(word) < 5 else print("word > 5 letters")

print()

# General syntax:
# [code] if [condition] else [alternate code]

# I want to change x based on word length

x = 10 if len(word) > 5 else 0 # otherwise, it's equal to 0
print(x)

x = -10 if len(word) < 5 else 0
print(x)

# If you're assigning using a ternary if statement, don't say "[name] =" twice
