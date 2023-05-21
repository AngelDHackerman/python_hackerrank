# Given the participants' score sheet for your University Sports Day, 
# you are required to find the runner-up score. You are given N scores. 
# Store them in a list and find the score of the runner-up (second higher score).

def find_runnerUP (n, array):
  max_value = max(array)
  while max_value in array: # This will remove any duplicate of any ocurrency 
    array.remove(max_value)
    
  second_max_value = max(array)
  return second_max_value

if __name__ == '__main__':
  n = int(input())
  arr = input()
  array = list(map(int, arr.split())) # change the input string, into a list of integers. 
  print(find_runnerUP(n, array))