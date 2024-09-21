# Write your function, here.
def is_palindrome(str):
  reverse = ''.join(reversed(str))
  print(reverse)
  return str == reverse


print(is_palindrome("kayak")) # True
print(is_palindrome("app"))  # False
print(is_palindrome("racecar")) # True
print(is_palindrome("valid")) # False