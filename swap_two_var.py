# 1st Method 
x = 10
y = 20
temp = x  # temp = 10
x = y  # y = 20
y = temp # y = 10

print("x:", x)  # x = 20
print("y:", y)  # y = 10

# 2nd Method 
x = 5
y = 10

x, y = y, x
print("x:", x)
print("y:", y)