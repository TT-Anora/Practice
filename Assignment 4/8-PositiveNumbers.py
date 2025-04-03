from functools import reduce


def takeInput():
    values = []
    values = input("Enter the numbers with space: ").strip(" ").split(" ")
    values = list(map(int, values))
    return values

#Uses the filtered list which contains only positive values to find average
def getAvgOfPositives(numbers: list):
    sum = reduce(lambda x,y: (x+y) , list(filter(lambda x: x>0, numbers)))
    count = len(list(filter(lambda x: x>0, numbers)))
    return sum/count

numbers = takeInput()
print(getAvgOfPositives(numbers))