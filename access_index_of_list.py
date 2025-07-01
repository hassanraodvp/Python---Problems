# Solution 01 Using enumerate Method 

num = [85, 98, 99, 100, 101]

for index, value in enumerate(num, start=1):
    print(index, "- ", value)
    
# Solution 02 without using enumerate method 

num2 = [85, 98, 99, 100, 101]

for index in range(len(num2) ):
    value = num2[index]
    print(index, "- ", value) 