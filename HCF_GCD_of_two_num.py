# Highest Common Factor (HCF) of two numbers

import math
# Function to calculate HCF
def find_hcf(x, y):
    return math.gcd(x, y)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
hcf = find_hcf(num1, num2)
print(f"The HCF of {num1} and {num2} is {hcf}")