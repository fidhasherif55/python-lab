s=input("enter a sentence:")
print(s)
WordsList=s.split()
print(WordsList)
#use set to get unique words
uniqueWords=set(WordsList)
for word in uniqueWords:
    print(f"{word} occurs {WordsList.count(word)}times")
    
