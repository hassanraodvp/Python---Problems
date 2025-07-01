def sum_nat (n):
    if n <= 1:
        return n
    else:
        return n + sum_nat(n - 1)
# Get user input

n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    result = sum_nat(n)
    print(f"The sum of natural numbers up to {n} is: {result}")