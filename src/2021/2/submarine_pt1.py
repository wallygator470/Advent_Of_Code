import os

def main():
  screen_clear()
  print(directions(read_input()))

def directions(data):
  d = 0
  h = 0
  for input in data:
    dir, num = input.split()[0], int(input.split()[1])
    if dir == 'forward':
      x = h
      h += num
      #print 'horiz', x, ' + ', num, ' = ', h, ' <==> ', dir
    elif dir == 'down':
      x = d
      d += num
      #print 'depth', x, ' + ', num, ' = ', d, ' <==> ', dir
    elif dir == 'up':
      x = d
      d -= num
      #print 'depth', x, ' - ', num, ' = ', d, ' <==> ', dir
  #print 'depth: ', d, '- horiz: ', h
  return h * d

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