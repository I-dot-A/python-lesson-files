# you need this
from abc import ABC, abstractmethod

class Vehicle(ABC): # inherits from ABC
    # This is an abstract class, it's like blueprint for other classes that inherit from it
    # You can use abstract classes to indicate anything any child classes need to have
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod # abstract methods cannot be called
    def move(self):
        pass

class Car(Vehicle):
    def __init__(self, speed): # abstract methods must be overridden
        self.speed = speed
    
    def move(self): # abstract methods must be overridden
        print("vroom vroom")

class Plane(Vehicle):
    def __init__(self):
        self.wings = True

    def move(self):
        print("eeeeeeeeerrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
    
    def break_wings(self):
        self.wings = False

#vehicle = Vehicle() can't instantiate an abstract object
car = Car(100)
plane = Plane()
plane.move()
car.move()
plane.break_wings()
print(plane.wings)