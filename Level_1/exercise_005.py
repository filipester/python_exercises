# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters

class IO_String(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Digite sua string: ")

    def printString(self):
        print(self.s.upper())


strObj = IO_String()
strObj.getString()
strObj.printString()