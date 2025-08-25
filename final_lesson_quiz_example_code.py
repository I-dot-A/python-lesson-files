import time, unittest
from abc import ABC, abstractmethod

print(time.time())
print(unittest.loader)

nums = [6, 2, 3, 10, 9]
nums.insert(2, 0)

items = [4, 2, "Trevor", False, 6.7, "Aaron", True]
items[0], items[6] = items[6], items[0]
items[3] = 1.0
items[1] += 3
items[1], items[4] = items[4], items[1]
items[6] = items[5]
print(items)

items = {"Desmond", 2, "5", 6, 7}
items.pop()
print(items)

vehicle_speeds = {"car": 70, "train": 45, "plane": 600}

vehicle_speeds["unicycle"] = 8
vehicle_speeds.popitem()

nums = {1, 2, 3, 4, 5}
items = {"three": 3, "ten": 10, "cookies?": "delicious"}

if 6 not in nums:
    if not ("cookies?" in items and items["ten"] <= items["three"]):
        if len(items) > len(nums):
            print("A")
        else:
            print("B")
    elif 5 in nums and "ten" in items:
        if items["cookies?"] is "delicious":
            print("C")
        else:
            print("D")
    else:
        print("E")
else:
    print("F")

nums = (6, 7, 2, 4, 1, 10, 9, 0, 5)

if nums[3] == 2:
    print("A") if len(nums) == 9 else print("B")
elif nums[3] == 4:
    print("C") if nums[6] == 10 else print("D")
else:
    print("E")

nums = [5, 6, 7, 3]
nums2 = nums
nums3 = nums2.copy()

if nums is nums3 or nums[1:3] == [5, 6]:
    if nums[:2] == [5, 6, 7]:
        print("A")
    elif nums[2:] == [7, 3]:
        print("B")
    else:
        print("C")
elif nums is nums2 and nums[0] == [5]:
    if nums[3] == 3:
        print("D")
    else:
        print("E")
else:
    print("F")

for i in range(5):
    if i % 2 == 0:
        print("foo")
    else:
        print("bar")

nums = []

# assume nums is a list
# with an unknown length
for i in range(len(nums)):
    print(nums[i])

# assume nums is a list
# with an unknown length
for item in nums:
    print(item)

x = 10
while x < 0:
    print(x)
    x -= 1

def make_new_list(*nums):
    new_list = []
    for num in nums:
        new_list.append(nums[num])
    return new_list

items = make_new_list(4, 0, 3, 2, 1, 5)
print(items)

bananas = 3
name = "John Wick"

sentence = f'{name} has {bananas} bananas.'
print(sentence)

#x = int(input())
x = 2

if x > 0:
    print("x > 0")
elif x < 0:
    print("x < 0")
else:
    print("x = 0")

def plus_2(x):
    return x + 2

#num = int(input())
#y = plus_2(num)

def find_average(first, second):
    return (first + second) / 2

find_average(7, second = 10)

class Thing:
    def __init__(self, value):
        self.value = value
    
    def get_value(self):
        return self.value
    
    def set_value(self, new_value):
        self.value = new_value

thing = Thing(4)
thing.set_value(2)

class Doohickey:
    def __init__(self):
        self.num = 0

class NumCruncher:
    def mult_nums(self, nums):
        return self._mult_nums(nums[1:], nums[0])

    def _mult_nums(self, nums, output):
        if nums:
            output *= nums[0]
            return self._mult_nums(nums[1:], output)
        return output

class Stuff:
    word = "burrito"

    def __init__(self):
        self.num = 4

class Vehicle:
    def __init__(self, wheels, speed):
        self.num_wheels = wheels
        self.speed = speed
    
    def move(self):
        print("moves")

class Car(Vehicle):
    def __init__(self, wheels, speed, model):
        Vehicle.__init__(self, wheels, speed)
        self.model = model
    
    def move(self):
        print("vroom vroom")

car = Vehicle(4, 140)
car.move()

class Animal(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Cat(Animal):
    pass

