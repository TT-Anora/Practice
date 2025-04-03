A = [1, 2, 3, 4]
# beh
#uses list comprehension
def raiseTo(A: list, power: int):
    power = [x**power for x in A]

    return power

print(raiseTo(A, 2))
print(raiseTo(A, 3))
print(raiseTo(A, 4))
print(raiseTo(A, 5))