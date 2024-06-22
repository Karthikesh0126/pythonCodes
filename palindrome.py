def isPalindrome(s):
    return s == s[::-1]
 
s = input("Enter the String to check if it is Palindromic: ")
res = isPalindrome(s)
 
if (res):
    print("Yes, It is a palindromic String.")
else:
    print("No, It is NOT a Palindromic String.")