# You are given a string S and width W.
# Your task is to wrap the string into a paragraph of width W.

import textwrap

def wrap(string, max_width):
  # textwrap.wrap(s, w) first parameter is the string, second one is the with of each word.
  # textwrap.wrap(s, w) will return an array of the new substrings
  # "\n".join() will join the elements of the array but "separated" with new lines
  return "\n".join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
  string, max_width = input(), int(input())
  result = wrap(string, max_width)
  print(result)