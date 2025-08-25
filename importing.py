# how to import
import math, time
import imported # to import your own module, use the name of your own file
from imported2 import kenneth_chow, DoThing # I've only imported the kenneth_chow and DoThing class

if __name__ == "__main__":
    print(math.sqrt(16))
    print(time.time())
    imported.neil_pandya()
    kenneth_chow()
    thing = DoThing(100)
    thing.print_value()