import os

def main():
  screen_clear()
  print(directions(read_input()))

def directions(data):
  d = 0
  h = 0
  a = 0
  for input in data:
    dir, num = input.split()[0], int(input.split()[1])
    if dir == 'forward':
      x = h
      y = d
      d += (a * num)
      h += num
      #print 'd:', d, ' - h: ', h, ' - a: ', a
      #print 'horiz', x, ' + ', num, ' = ', h
      #print 'depth', y, ' + ', num, ' = ', d, ' <==> ', dir
    elif dir == 'down':
      x = a
      a += num
      #print 'd:', d, ' - h: ', h, ' - a: ', a
      #print 'aim', x, ' + ', num, ' = ', a, ' <==> ', dir
    elif dir == 'up':
      x = a
      a -= num
      #print 'd:', d, ' - h: ', h, ' - a: ', a
      #print 'aim', x, ' - ', num, ' = ', a, ' <==> ', dir
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