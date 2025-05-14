# Solution 01 using ' | ' operator 

Dict1 = {"Hassan": 76, "Ali": 87, "Ahmed": 67}
Dict2 = {"Hassan": 86, "Khalid": 89, "Hamza": 67}

print(Dict1 | Dict2)

# Solution 02 using ' ** ' method

Dic3 = {"Hassan": 76, "Ali": 87, "Ahmed": 67}
Dict4 = {"Hassan": 86, "Khalid": 89, "Hamza": 67}

print({**Dic3, **Dict4})

# Solution 03 using ' copy(), update() ' method

Dic5 = {"Hassan": 76, "Ali": 87, "Ahmed": 67}
Dic6 = {"Hassan": 86, "Khalid": 89, "Hamza": 67}

updateDict = Dic5.copy()
updateDict.update(Dic6)
print(updateDict)