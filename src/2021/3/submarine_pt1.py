import os

def main():
  screen_clear()
  data = read_input()
  print get_power_consumption(data)

def split_binary(data):
  all_num_parts = []
  for record in data:
    num_parts = list(record)
    all_num_parts.append(num_parts)
  return all_num_parts
  
def get_power_consumption(data):
  lb = len(data[0])
  la = len(data)
  g = []
  e = []
  comp = int(la) / 2
  arr = split_binary(data)
  for i in range(lb):
    s = sum(int(part[i]) for part in arr)
    if s >= comp:
      g.append('1')
      e.append('0')
    else:
      g.append('0')
      e.append('1')
  gamma = int(''.join(g), 2)
  epsilon = int(''.join(e), 2) 
  return gamma * epsilon

def read_input():
  with open('input.txt', 'r') as file:
    data = [line.strip() for line in file.read().splitlines()]
  return data

def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

main()