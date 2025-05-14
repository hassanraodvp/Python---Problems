a = input("Enter Something here you want to sort: ")

word = a.split()

for i in range(len(word)):
    word[i] = word[i].lower()
word.sort()
print("The sorted words are:", word)