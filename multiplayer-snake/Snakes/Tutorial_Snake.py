from Snake import Snake

class my_snake(Snake):

  def is_safe(self, x, y):
    field = self.game.field

    # add index check later
    height = len(field)
    width = len(field[0])
    if (x >= width or x < 0 or y >= height or y < 0):
      return False

    return field[y][x][-1] in [' ', 'A']

  def update_controls(self):
    field = self.game.field

    print()
    for row in field:
      for col in row:
        if col[-1] == ' ':
          print('.', end='')
        else:
          print(col[-1], end='')
      print()

    # for row_num in range(len(field)):
    #   for col_num in range(len(field[0])):
    #     print(field[row_num][col_num])

    for row_num in range(len(field)):
      for col_num in range(len(field[0])):
        if field[row_num][col_num][-1] == 'A':
          apple_y = row_num
          apple_x = col_num

    x = self.pos.x
    y = self.pos.y

    if apple_y > y:
      self.direction = 'down'
    elif apple_y < y:
      self.direction = 'up'
    elif apple_x > x:
      self.direction = 'right'
    elif apple_x < x:
      self.direction = 'left'

    for i in range(2):
      if self.direction == 'up':
        if not self.is_safe(x, y-1):
          self.direction = 'right'
      if self.direction == 'right':
        if not self.is_safe(x+1, y):
          self.direction = 'down'
      if self.direction == 'down':
        if not self.is_safe(x, y+1):
          self.direction = 'left'
      if self.direction == 'left':
        if not self.is_safe(x-1, y):
          self.direction = 'up'

    print(self.direction)