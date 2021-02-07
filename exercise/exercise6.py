string=input("Enter the word");
reverseWord=""
for i in reversed(range(len(string))):
    reverseWord+=string[i]
result="string is a palindrome" if string==reverseWord else "string isnt a palindrome";
print(result);