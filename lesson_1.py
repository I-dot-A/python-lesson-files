print("Hello, world!")

# This is a single-line comment

""" This is a
multi-line
comment """

# [name] = [value]
x = 2
word = "four" # = in Python means assignment
print(x)
print(word)
print()

print(2 + 2, "addition")
print(2 - 2, "subtraction")
print(2 * 3, "multiplication")
print(4 / 2, "division")
print(4 // 2, "floor division") # Rounds answer down, returns an int
print(5 // 2, "floor division 2.5 --> 2")
print(3 % 2, "modulo")
print(2 ** 4, "exponentiation")

y = z = 3 # Defines multiple variables to the same value in one line
print(y)
print(z)

a, b = 1, 2 # Defines multiples variables to different values in one line
print(a)
print(b)

print()

x = 2.4 # float (decimal)
a = True # boolean
b = False 

# Snake case to name variables (all lowercase, underscores between words)
like_this = "tree"
or_this_you_feel_me = "?"

to_str = str(x) # x is an float, but we cast it to a string
print("to_str is a", type(to_str)) # type() returns the type of the variable

print()

"""LISTS"""
# Mutable (changeable)
# Ordered (0-indexed, have a fixed order)

# name = [items]
nums = [1, 2, 3, 4, 5]
print(nums)

# To add to the list, 2 methods:
# .append(item) --> adds to the end of the list
nums.append(6)
print(nums, ".append(6)")

# .insert(index, item) --> adds an item to an index,
# pushing all items at that index and onward forward 1
nums.insert(3, 0)
print(nums, ".insert(3, 0)")

# To remove from the list, 3 methods:
# .pop() --> pops from the end of the list, returns the value popped
x = nums.pop()
print(x) # x = 6
print(nums, ".pop()")
nums.pop() # Using .pop() again
print(nums, ".pop() again")
# OR .pop(index) --> pops from an index, returns the value popped
nums.pop(0) # 1 should be removed
print(nums, ".pop(0)")

# .remove(item) --> remove the first occurence of a specified item
nums.append(0) # Adding a duplicate 0
print(nums)
nums.remove(0)
print(nums, ".remove(0)") # Removed the first 0, not the second 0

# .clear() --> clears the list
nums.clear()
print(nums, ".clear()")

print()

# Other methods:
# .copy()
nums = [5, 3, 1, 2, 4]
nums_copy = nums.copy() # Makes a copy of the specified list (nums)
print(nums, "nums")
print(nums_copy, "nums_copy")

# .sort()
nums.sort() # Sorts the list
print(nums, ".sort()")
print()

# Accessing indices
print(nums[0], "nums[0]") # Accesses the first index

nums[0] = 10
print(nums, "nums[0] = 10")

nums[0], nums[4] = nums[4], nums[0] # Swaps index 0 and index 4 in one line
print(nums, "after swapping i = 0 and 4")

print()

nums = [1, 2, 3, 4, 5, 6, 7]
# List slicing
print(nums[1:4]) # Print a list of nums from i = 1 to i = 3 (exlusive of 4)

less_nums = nums[0:3]
print(less_nums, "= nums[0:3]")

print(nums[2:], "nums[2:]") # Goes from i = 2 to the end of the list

print(nums[:5], "nums[:5]") # Goes from beginning of the list to i = 4

print()

# Negative indexing
print(nums[-1], "nums[-1]") # Prints from the last index of the list
print(nums[-2], "nums[-2]") # Prints from the second-to-last index

# Adding lists together
words = ["apple", "banana", "2018 Toyota RAV4"]
names = ["Neil", "Kenny", "Peter Griffin", "Solid Snake", "Joe"]

# Using '+'
stuff = words + names
print(stuff)

# .extend()
words.extend(names)
print(words)

words = words + names # + is easier imo
print(words)

"""TUPLES"""
# Immutable (not changeable)
# Ordered (0-indexed, fixed order)
# name = (stuff)
nums_tuple = (4, 5, 3, 2)

# Acess indices, but not change them
print(nums_tuple[1], "index 1")
# nums_tuple[1] = 837498728397983 This doesn't work

# len()
# Returns the length of a list, tuple, set, dictionary, or string
print(len(nums_tuple)) # Should be 4
print(len([1, 2, 3, 323432])) # Should be 4





























