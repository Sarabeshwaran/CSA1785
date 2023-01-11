Input:

my_str=str(input("Enter the sentence you want to sort: "))
words=[word.lower() for word in my_str.split()]
words.sort()
print("The Sorted words are:")
for word in words:
    print(word)
    
Output:

Enter the sentence you want to sort: Banana Greenapple Apple Pineapple
The Sorted words are:
apple
banana
greenapple
pineapple
