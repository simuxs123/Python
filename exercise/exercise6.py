string=input("Enter the word");
reverseWord=""
for i in reversed(range(len(string))):
    reverseWord+=string[i]

if string==reverseWord:
    print("string is a palindrome")
else:
    print("string isnt a palindrome")