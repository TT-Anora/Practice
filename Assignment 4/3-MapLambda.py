"""
Slightly modified the lists,
so that even if the maker name is not the first string in the model,
it can still correctly identify the models without names
Added Elanatra Hyundai to the car_models
"""

car_makers = ["Honda", "Toyota", "Ford", "Nissan", "Hyundai"]
car_models = ["Honda Civic", "Honda Accord", "Toyota Corolla", "Toyota Camry", "Ford Fusion", "Ford Escape", "Nissan Sentra", "Hyundai Elantra", "Elantra Hyundai"]

#Splits it into lists using " " and accesses the list using index 0 or 1
myList = list(map(lambda model:
                  model.split(" ")[1 if model.split(" ")[1] not in car_makers else 0],
                  car_models))


print(myList)