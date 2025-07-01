# Using enumerate() 
l = [23, 45, 67, 89]
for index, value in enumerate(l):
    print(index, "-", value)

# without Using enumerate
l = [23, 45, 67, 89]
for i in range(len(l)):
    print(i, "-", l[i])