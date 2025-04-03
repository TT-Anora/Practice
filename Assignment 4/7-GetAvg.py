from functools import reduce


def takeInput():
    values = []
    values = input("Enter the numbers with space: ").strip(" ").split(" ")
    values = list(map(int, values))
    return values

def getAvg(numbers: list):
    return reduce(lambda x,y: (x+y), numbers)/len(numbers)


numbers = takeInput()
print(getAvg(numbers))