# Using the dictionary method fromkeys() to count the number of vowels in a string 
name = input("Enter your name: ")

voswels = "aeiou"

name = name.casefold()
count = {}.fromkeys(voswels, 0)

for char in name:
    if char in count:
        count[char] += 1

print(count)

# Using List and Dictionary Comprehension 

name2 = input("Enter your name: ")
voswels = "aeiou"

name2 = name2.casefold()

count = {key:sum([1 for char in name2 if char == key]) for key in voswels}
print(count)