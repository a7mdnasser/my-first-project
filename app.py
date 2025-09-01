def is_palindrome(s):
    s=s.lower().replace(" ","")
    return s==s[::-1]
text = input("Enter a text: ")
if is_palindrome(text):
    print(text+" is palindrome")
else:
    print(text+ " is not palindrome")
