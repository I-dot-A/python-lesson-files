# In Python, there are classes
class Car: # class [name]:
    # __init__ is a dunder method, which is a method provided by Python, but you can change it
    # self means that this method or variable is part of this instance
    def __init__(self): # init stands for initialize
        """Constructor"""
        self.model = "2017 Toyota RAV4" # This is an instance variable because of the self keyword
        self.color = "silver"

    def honk(self): # you need self or it will not work
        print("HONK")
    
    def get_color(self): # getter
        """Gets the color of the car"""
        return self.color # you need the self keyword to call instance variables
    
    def set_color(self, new_color): # setter, include parameters after self
        """Sets the color of the car"""
        self.color = new_color

# [name] = Object()
car = Car() # this is how you instantiate a new object

car.honk() # Calls the honk method for the car instance
print(car.get_color())

car2 = Car() # another instance
car2.set_color("red")
print(car2.get_color())

print()

class ImprovedCar: # all caps, no spaces for class names
    num_wheels = 4 # this remains the same for all instances of ImprovedCar

    def __init__(self, brand, model, color, max):
        self._brand = brand # single underscore indicates that this is private
        self._model = model
        self._color = color
        self._max_speed = max
    
    def honk(self): # you need self or it will not work
        print("HONK")
    
    def get_color(self): # getter
        """Gets the color of the car"""
        return self._color # you need the self keyword to call instance variables
    
    def set_color(self, new_color): # setter, include parameters after self
        """Sets the color of the car"""
        self._color = new_color

better_car = ImprovedCar("Toyota", "2019 Highlander", "Mahogany", 135)
print(better_car.get_color())
better_car._model = "lol"
print(better_car._model) # Unfortunately, in Python, there's no way to actually make a variable private
                         # Single underscore is the standard convention to indicate that it's private
                         # Tells others devs this is private, please don't touch it outside the class
                         # Single underscore also indicates that a method is private (Example: def _do_thing(self): [code])

another_car = ImprovedCar("Bogus", "Speedy", "Smaragdine", 2)
print(better_car.num_wheels)
print(another_car.num_wheels) # This is printing the class variable num_wheels.
another_car.num_wheels = 3 # This does not change the value of num_wheels. Instead, it instantiates a new instance variable called num_wheels for another_car.
print(better_car.num_wheels)
print(another_car.num_wheels) # This is printing an instance variable called num_wheels.
print(ImprovedCar.num_wheels) # This directly accesses the class variable.
ImprovedCar.num_wheels = 26 # This changes for all instances.
print(better_car.num_wheels) # this is now 26

# The main difference between a class variable and instance variable is that instance variables are unique for each 
# instance of a class, while class variables are the same for all instances of a class.

class ListStuff:
    def binary_search(self, nums, target):
        return self._binary_search(nums, target, 0, len(nums) - 1) # calling a private method
    
    def _binary_search(self, nums, target, left, right):
        median = (left + right) // 2
        if nums[median] == target: # base case to prevent infinite looping
            return True
        elif left >= right: # base case if the target is not in the list
            return False
        elif nums[median] > target:
            return self._binary_search(nums, target, left, median)
        else:
            return self._binary_search(nums, target, median, right)

thing = ListStuff()

big_list = [i for i in range(1, 10001)]

print(thing.binary_search(big_list, 6941))