def ASCII(words: list):
    return [ord(x) for x in words]

words = input("Enter string: ")
print(ASCII(words))

