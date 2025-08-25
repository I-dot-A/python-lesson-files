# range(x) --> returns a range of ints from 0 to x - 1
nums = [i for i in range(10)]
print(nums) # The range is 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# range(x, y) --> returns a range of ints from x to y - 1
nums = [i for i in range(2, 8)]
print(nums) # The range is 2, 3, 4, 5, 6, 7

# range(x, y, z) --> returns a range of ints from x to y - 1, increment by z
nums = [i for i in range(3, 12, 2)]
print(nums) # The range 3, 5, 7, 9, 11

print()

"""FOR LOOPS"""
# Syntax: for [var] in range([int]): [code]
for i in range(3):
    print("Hello")

for i in range(3):
    print(i)

print()

# You can't change the number of increments for a standard for loop
for i in range(5):
    print(i, "Before decrement")
    i -= 1 # Subtracts i by 1
    print(i, "After decrement")
# The range here is 0 to 4, so in a standard for loop, you are
# literally iterating through a range of numbers

print()

# Make sure you indentations are correct
for i in range(3):
    print(i + 1)
print("1 iteration completed")

print()

# Iterating using len
list_1 = [3, 2, 1, 3, 267]
for i in range(len(list_1)):
    print(list_1[i])

print()

tuple_1 = (1, 2, 3, 4, 999)
for i in range(len(tuple_1)):
    print(tuple_1[i])

print()

"""FOR EACH LOOPS"""
# Syntax: for [item] in [items]: [code]
# For each loops are better for sets and dictionaries

set_1 = {1, 2, 3, 4, 5}
for num in set_1: # For every number in set_1
    print(num)

print()

words = {"fork", "spoon", "1999 Toyota Corolla", "pancake", "Johnathan Arbuckle"}
for word in words:
    print(word)

print()

nums = [1, 2, 3]
for num in nums:
    print(num)

print()

dictionary = {"car": "2000 Honda Pilot", "bus": "Bus 20",
              "plane": "Boeing", "motorcycle": "vroom vroom"}

for item in dictionary:
    print(item) # Prints key
    print(dictionary[item]) # Prints value

print()

"""WHILE LOOPS"""
# Syntax: while [condition]: [code]
x = 4 # The variable is pre-defined
while x > 0:
    print(x)
    x -= 1 # You can change the looping variable in a while loop

print()

names = ["Student 1", "Self-Proclaimed Professor Alsubai",
         "Student 2", "Spongebob Squarepants", "Peter Griffin"]

while names: # Checks if the list is not empty:
    print(names.pop()) # Print each name that gets removed

print()

"""F-STRINGS"""
x = 2
name = "Sally"
print(f"{name} has {x} apples.")

# Syntax: f"{var}"

print()

"""FUNCTIONS"""
# Syntax: def name(parameter): [code]
def print_hello_world(): # def is the keyword to define a function
    print("Hello, world!")

print_hello_world() # Calling the function

def add_one(num): # num is a parameter
    num += 1
    return num # return is the keyword to return a value
               # If there is no return value, it returns None, making
               # it a void function.

x = add_one(2) # Here, 2 is an argument

print(x) # x = 3

# If there is one parameter, you can only include one argument, no more no less
#y = add_one() # Error
#z = add_one(1, 2) # Error

def print_word(word):
    """Prints a given word""" # This is a docstring, which describes
                              # what a function does
    print(word)

print_word("lol")

print()

def add_two_nums(num1 = 0, num2 = 0):
    """Adds two numbers together"""
    return num1 + num2

x = add_two_nums() # With default values, I no longer need to specify
                   # the arguments
print(x)

x = add_two_nums(4) # 4 + 0
print(x)

x = add_two_nums(4, 2) # 4 + 2
print(x)

x = add_two_nums(num1 = 4) # 4 + 0
print(x)

x = add_two_nums(num2 = 6) # 0 + 6
print(x)

# With keyword arguments, order does not matter
x = add_two_nums(num2 = 10, num1 = 5) # 5 + 10
print(x)

print()

# Arbitary arguments
def find_sum(*nums): # * indicates an arbitary argument, it's a tuple
    output = 0
    for num in nums:
        output += num
    return output

print(find_sum(4, 5, 6, 7)) # Give it a tuple of arguments (separate by ,)
print(find_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
print(find_sum())

print()

# Arbitary keyword arguments (often called kwargs)
def do_thing(**items): # ** indicates an arbitrary keyword argument,
                       # items is a dictionary
    for item in items:
        print(item)
        print(items[item])

do_thing(name = "Jeb", age = "38", hobby = "Basketball")
# You give it a dictionary of arguments

print()

"""INPUT AND TRY/EXCEPT"""
""" x = input() # Takes an input from the user
print(x)

word = input("Give me a word\n") # Can also print a statement
print(word) """ # Uncomment to check this code out

# I want an integer, not a string
#num = int(input("Give me a number between 1 and 100\n")) # This could cause errors
#print(num)

try: # try to do this
    num = int(input("Give me a number between 1 and 100\n"))
    if num > 100 or num < 1:
        raise TypeError # raise raises an error
    print(f"Your number: {num}")
except ValueError: # do this if a ValueError occurs
    print("You did not give a number")
except TypeError: # do this if a TypeError occurs
    print("You gave a number too big or too small")
except Exception: # do this if any other error occurs
    print("Something went wrong")
finally: # This code runs regardless if there's an error or not
    print("Thanks for playing")

print()

def two_nums():
    """Adds two given numbers from user in terminal"""
    while True:
        try:
            num1 = int(input("Give me a number\n"))
            break
        except ValueError:
            print("Please give a number")
    while True:
        try:
            num2 = int(input("Give me another number\n"))
            break
        except ValueError:
            print("Please give a number")
    return num1 + num2

print(f"Answer is: {two_nums()}")

print()

# Anonymous functions
z = lambda a : a + 2

print(z(2))

# z is the anonymous function
# a is a parameter
# lambda defines the anonymous function
# To the right of the colon is what the function does

def to_power(num):
    """Returns an anonymous function that exponentiates to a given power"""
    return lambda a : a ** num

power_4 = to_power(4) # power_4 is an anonymous function

print(power_4(4)) # printing 4 to the power of 4
































