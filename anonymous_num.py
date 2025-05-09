# Square using Anonymous Function 

nTerms = int(input("Enter number of terms: "))

result = list(map(lambda x: 2 ** x, range(nTerms + 1)))
print("Square root of first", nTerms, "terms are:", result)

for i in range(nTerms + 1):
    print(f"The value of 2 raised to the power of {i} is: {result[i]}")
    
# Power of 2 using Anonymous Function     
nTerms2 = int(input("Enter number of terms: "))

result = list(map(lambda x: x ** 2, range(nTerms + 1)))
print("Square root of first", nTerms, "terms are:", result)

for i in range(nTerms + 1):
    print(f"The value of {i} raised to the power of 2 is: {result[i]}")    
    