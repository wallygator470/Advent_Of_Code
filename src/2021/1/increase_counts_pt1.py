import os

def main():
  screen_clear()
  print(count_increases(read_input()))

def count_increases(data):
  cnt = 1
  for i, num in enumerate(data):
    if i == 0:
      next
    else:
      if data[i] > data[i - 1]:
        cnt += 1
  return cnt

def read_input():
  with open('input.txt', 'r') as file:
    data = list(file)
  return data

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()