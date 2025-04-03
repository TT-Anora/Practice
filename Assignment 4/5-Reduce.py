from functools import reduce

car_models = ["Honda Civic", "Honda Accord", "Toyota Corolla", "Toyota Camry", "Ford Fusion", "Ford Escape", "Nissan Sentra", "Hyundai Elantra"]

#Splits it into lists using " "
myList = reduce(lambda x, y: x.split(" ")[0 if len(x.split(" ")) == 1 else 1] + "," + y.split(" ")[1], car_models)

print(myList)