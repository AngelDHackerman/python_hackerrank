# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

# a = "-".join(a)

def split_and_join(line):
  splied = line.split(" ")
  joined = "-".join(splied)
  return joined

if __name__ == '__main__':
  line = input()
  result = split_and_join(line)
  print(result)