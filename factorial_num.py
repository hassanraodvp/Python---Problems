# Using For Loops 
num = int(input("Enter the number: "))

factorial = 1

if num < 0:
    print("Factorial does't exist")
if num == 0:
    print("Factorial of Zero is", 1)
if num > 0:
    for i in range(1, num + 1):
        factorial = factorial * i
print("The Factorial of given no. is", factorial)		

# Using Recursion 

def fact(a):
    if a == 0:
        return 1
    else:
        return ((a) * fact(a - 1))     
number = int(input("Enter the number: "))
result = fact(number)
print(f"The Factorial of {num} is ", result)






