def fac_of_num(n):
    if n == 1:
        return 1
    else:
        return n * fac_of_num(n - 1)
    
n = int(input("Enter the number: "))

if n == 0:
    print("Factorial of Zero is", 1)
elif n < 0:
    print("Factorial does't exist")
else:
    result = fac_of_num(n)
    print(f"The Factorial of {n} is ", result)    