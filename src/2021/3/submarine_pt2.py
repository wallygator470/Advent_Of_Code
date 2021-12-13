import os

def main():
  screen_clear()
  data = read_input()
  l = len(data[0])
  all_parts =  split_binary(data)
  ck = get_binary(all_parts, 0, 0)
  for i in range(1, l):
    ck = get_binary(ck, i, 0)
    #print(ck)
    if len(ck) == 1:
      break
  ok = get_binary(all_parts, 0, -1)
  for i in range(1, l):
    ok = get_binary(ok, i, -1)
    if len(ok) == 1:
      break
  co2 = int(''.join(ck[0]), 2)
  oxy = int(''.join(ok[0]), 2)
  print co2 * oxy

def get_common(arr, pos, factor):
  ones = 0
  zeroes = 0
  for binary in arr:
    if int(binary[pos]) == 0:
      zeroes += 1
    else:
      ones += 1
  if zeroes == ones:
    return 2
  elif zeroes > ones:
    return abs(0 - factor)
  else:
    return abs(1 - factor)

def get_binary(arr, i, factor):
  l = len(arr)
  mc = get_common(arr, i, factor)
  #print arr, i, mc
  new_arr = []
  for part in arr:
    #print part, mc, i, part[i], l, factor
    if mc == 2 and int(part[i]) == factor + 1:
      new_arr.append(part)
    elif int(part[i]) == mc and l > 1:
      new_arr.append(part)
  #print new_arr
  return new_arr

def split_binary(data):
  all_num_parts = []
  for record in data:
    num_parts = list(record)
    all_num_parts.append(num_parts)
  return all_num_parts

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