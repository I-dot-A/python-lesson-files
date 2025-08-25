# how to import
import math, time
import imported # to import your own module, use the name of your own file
from imported2 import does_something_else, DoThing # I've only imported the does_something_else and DoThing class

if __name__ == "__main__":
    print(math.sqrt(16))
    print(time.time())
    imported.does_something()
    does_something_else()
    thing = DoThing(100)
    thing.print_value()