""" python module has a special variable called __name__.
if the module is run as the main program, __name__ is set to "__main__".
if the module is imported into another program, __name__ is set to the module's filename """

# if this is executed directly then it will print __main__
# if this is executed via import then this will print filename
print(__name__)


def hi():
    print("hi hello sasrikal namasthey.....")

hi()

# now if we import this then the function hi() will fun once when imported and once when we call it (2 times) which is undesirable
# hence to solve this we use main guard

if __name__ == "__main__":
    hi()
# hence now if this file is imported  __name__ is file name not __main__ hence this will not run on import and only runs when called
    