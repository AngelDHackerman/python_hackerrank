#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
  # This line of code works in the following way: 
  # 1. `s.split(' ')` splits the string `s` into a list of words based on the space delimiter.
  # 2. `[i.capitalize() for i in s.split(' ')]` is a list comprehension that capitalizes each word in the resulting list from `s.split(' ')`.
  # 3. `' '.join([...])` concatenates all the words in the list back into a string, with a space between each word.
  # The result is that this line of code returns the original string but with each word capitalized.
  return ' '.join([i.capitalize() for i in s.split(' ')])


if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  s = input()
  result = solve(s)
  fptr.write(result + '\n')
  fptr.close()