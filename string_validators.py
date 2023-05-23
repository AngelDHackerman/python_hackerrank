# You are given a string S.
# Your task is to find out if the string S contains: alphanumeric characters, 
# alphabetical characters, digits, lowercase and uppercase characters.

# we used a list comprehension in the structure of the for loop
# the any() function will return "True" if any of the iterations returns "True"
# all() function will return "True" only if all the iterations returns "True"

if __name__ == '__main__':
  s = input()
  has_alnum = any(char.isalnum() for char in s)
  print(has_alnum)
  
  has_alpha = any(char.isalpha() for char in s)
  print(has_alpha)
  
  has_digit = any(char.isdigit() for char in s)
  print(has_digit)
  
  has_lower = any(char.islower() for char in s)
  print(has_lower)
  
  has_upper = any(char.isupper() for char in s)
  print(has_upper)