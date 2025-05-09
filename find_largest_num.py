num1 = float(input("Enter a number 01: "))
num2 = float(input("Enter a number 02: "))
num3 = float(input("Enter a number 03: "))

if (num1 > num2) and (num1 > num3):
    print("The largest number is", num1)
elif (num2 > num1) and (num2 > num3):
    print("The largest number is", num2)
elif (num3 > num1) and (num3 > num2):
    print("The largest number is", num3)
else:
    print("The numbers are equal")