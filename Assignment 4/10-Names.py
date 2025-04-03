list_ = ["Tarun Tambrahalli", "Jim Sinclair", "Rowan Atkinson", "Ramirez D'Angelo"]

myDict_ = {x.split(" ")[1]:x.split(" ")[0] for x in list_}

print(myDict_)