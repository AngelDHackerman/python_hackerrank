# In this challenge, the user enters a string and a substring. 
# You have to print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left.


# startswith() check if the string starts with the substring we passed in the first parameter
# the second parameter "i", indicates to startswith() where to start to check.

def count_substring(string, sub_string):
  count = 0
  for i in range(len(string)):
    if string.startswith(sub_string, i): 
      count += 1
  return count

if __name__ == '__main__':
  string = input().strip()
  sub_string = input().strip()
  
  count = count_substring(string, sub_string)
  print(count)