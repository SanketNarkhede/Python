def reverse(str1): 
    return str1[::-1] 
  
def isPalindrome(str1): 
    # Calling reverse function 
    rev = reverse(str1) 
  
    # Checking if both string are equal or not 
    if (str1 == rev): 
        return True
    return False
  
  

str1 = input("Enter a String: ")
ans = isPalindrome(str1) 
  
if ans == 1: 
    print("It is a palindrome") 
else: 
    print("It is not a palindrome") 