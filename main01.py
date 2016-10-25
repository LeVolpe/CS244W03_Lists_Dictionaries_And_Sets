import sys

def getInput():
    for line in sys.stdin:
        return line

def calculateProduct(a, b):
    print(a * b)

numberOne = int(getInput())
numberTwo = int(getInput())


calculateProduct(numberOne, numberTwo)


