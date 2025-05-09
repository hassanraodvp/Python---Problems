# num = int(input("Enter a number: "))
def ConvertBinary(num):
    if num > 0:
        ConvertBinary(num // 2)
        print(num % 2, end=' ')
num = int(input("Enter a number: "))        
print(f"The Binary of {num} is: ")
ConvertBinary(num)