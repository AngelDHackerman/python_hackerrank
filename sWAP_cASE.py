
# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
  return s.swapcase()  # this method swapcase() will change the case of each letter in the string.

if __name__ == '__main__':
  s = input()
  result = swap_case(s)
  print(result)