def takeInput():
    values = []
    values = input("Enter the numbers with space: ").strip(" ").split(" ")
    values = list(map(int, values))
    return values

def CtoF(list_: list):
    return [(lambda t: (t*9/5) + 32)(t) for t in list_]
    #lambda function is not even required but asked in the question


celsius_list = takeInput()
print(CtoF(celsius_list))