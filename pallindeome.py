s=input("Enter a word to check if it is a palindrome: ")
if s == s[::-1]:
    print(s,"is a palindrome ")
else:
    print(s,"is not a palindrome")