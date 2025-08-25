"""SCOPE"""
x = 2 # this is a global variable, can be accessed from anywhere
print(x + 2)

def x_plus_2():
    return x + 2
print(x_plus_2())

class Thing:
    def x_plus_3(self):
        return x + 3
thing = Thing()
print(thing.x_plus_3())

def change_x(num):
    global x # this allows x to be changed from within the function
             # without this, a different local x variable is instantiated
    x = num

change_x(4)
print(x)

class Thing2:
    global x # you need global to access the global variable x
             # within a class as well, otherwise, a class variable x is instantiated
    x = 3
    y = 10 # class variable y

    def print_y():
        # y does not exist until we define y
        y = Thing2.y # new local y = class variable y
        # OR directly print Thing2.y
        print(f"y = Thing2.y --> {y} or print(Thing2.y) --> {Thing2.y}")
    
    def something():
        z = 12 # local variable z
        print(z) # local
        print(Thing2.z) # class z
    z = 9 # class variable z

print(x) # changed from 4 to 3 inside the Thing2 class
Thing2.print_y()

print()

def do_something():
    word = "three"
    print(word)

word = "four" # a different word variable, local variables cannot be accessed outside of their local scope
print(word) # prints global word --> four
do_something() # prints local word inside do_something --> three

Thing2.something()

"""INHERITANCE AND POLYMORPHISM"""
# Inheritance is the idea that you can inherit traits and behaviors from another object
# Polymorphism is the idea that something that can many forms

class Vehicle:
    def __init__(self, wheels, speed):
        self.num_wheels = wheels
        self.speed = speed
    
    def move(self):
        print("moves")

class Car(Vehicle): # To inherit another class, put the other class(es) in parentheses after the name
    def __init__(self, wheels, speed, model):
        Vehicle.__init__(self, wheels, speed) # calling the parent constructor
        self.model = model
    
    def move(self): # method overriding
        print("vroom vroom")

class Plane(Vehicle):
    def __init__(self, wheels, speed, wingspan):
        Vehicle.__init__(self, wheels, speed)
        self.wingspan = wingspan
    
    def move(self):
        print("eeeeeeeeeeeeeerrrrrrrrrrrrrrrrrrrrr")

class UnknownContraption(Vehicle):
    def __init__(self, wheels, speed):
        super().__init__(wheels, speed)

vehicle = Vehicle(3, 100)
car = Car(4, 135, "2018 Nissan Rogue")
vehicle.move()
car.move()
plane = Plane(6, 600, 150)
plane.move()
print(car.num_wheels)
print(plane.speed)
moving_thing = UnknownContraption(1, 1)
moving_thing.move() # this prints the parent move method

print()

# The fact that .move(), the same method, does many different things depending on the circumstance
# is an example of polymorphism.

# .pop() is also polymorphic
# list.pop() removes the last item from a list
# but set.pop() removes a random item from a set
# dict.pop() removes a specified item from a dictionary
# Basically, .pop(), despite having the same name, does many different things
nums = [1, 2, 3, 4]
nums.pop()
print(nums)

nums_set = {1, 2, "three", "four"}
nums_set.pop()
print(nums_set)