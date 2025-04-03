"""
This is the solution for the requested question
but the zip function only iterates for the smallest list
and also the maker and the models don't match
so I tried to implement both the ways
"""
car_makers = ["Honda", "Toyota", "Ford", "Nissan", "Hyundai"]
car_models = ["Honda Civic", "Honda Accord", "Toyota Corolla", "Toyota Camry", "FordFusion", "Ford Escape", "Nissan Sentra", "Hyundai Elantra"]

# myDict = {car_makers[x]:[car_models[y],car_models[y+1]]
#           for x, y in
#           zip(range(len(car_makers)),
#               range(0,len(car_models),2))}
#
# print(myDict)


myDict = {maker : [model for model in car_models if maker in model] for maker in car_makers}
# not using zip but works
print(myDict)