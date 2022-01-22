from Snake import Snake
import random

class Enemy_Snake(Snake):
  def init(self):
    body_color = (random.randint(10, 255), random.randint(0, 255), random.randint(10, 255))
    tail_color = []
    for i in range(3):
      tail_color.append(max(0, min(255, body_color[i] + random.uniform(-100, 100))))
    self.set_color(body_color, tail_color)
    self.header = random.randint(0, 1)
        
  def get_spot(self, x, y):
    if y >= len(self.game.field):
      return '#'
    elif y < 0:
      return '#'
    elif x < 0:
      return '#'
    elif x >= len(self.game.field[0]):
      return '#'

    return self.game.field[y][x][-1]

  def is_safe(self, direction, predict):
    if direction == 'up':
      x = self.pos.x
      y = self.pos.y - 1
    elif direction == 'right':
      x = self.pos.x + 1
      y = self.pos.y
    elif direction == 'down':
      x = self.pos.x
      y = self.pos.y + 1
    elif direction == 'left':
      x = self.pos.x - 1
      y = self.pos.y

    space = self.get_spot(x, y)

    if space in [' ', 'A']:
      if predict:
        spots = [self.get_spot(x - 1,y), \
                 self.get_spot(x,y - 1), \
                 self.get_spot(x + 1,y), \
                 self.get_spot(x,y + 1)]
        spots = [spot for spot in spots if type(spot) == int]
        if len([1 for spot in spots if spot % 2 == 0]) > 1:
          return False
      return True

    return False

  def set_horizontal_dir(self, x, y):
    if x > self.pos.x:
      self.direction = 'right'
    elif x < self.pos.x:
      self.direction = 'left'

  def set_vertical_dir(self, x, y):
    if y > self.pos.y:
      self.direction = 'down'
    elif y < self.pos.y:
      self.direction = 'up'

  def set_reverse(self):
    if self.direction == 'up':
      self.direction = 'down'
    elif self.direction == 'down':
      self.direction = 'up'
    elif self.direction == 'right':
      self.direction = 'left'
    elif self.direction == 'left':
      self.direction = 'right'

  def update_controls(self):
    #field = [[spot[-1] for spot in row] for row in self.field]
    # field = [[spot[-1] for spot in row] for row in self.game.field]
    # for row in field:
    #     print('|' + ''.join([str(i) for i in row]) + '|')
    # print()

    for y, row in enumerate(self.game.field):
      for x, spot in enumerate(row):
        if spot[-1] == 'A':
          if self.header:
            self.set_horizontal_dir(x, y)
            self.set_vertical_dir(x, y)
          else:
            self.set_vertical_dir(x, y)
            self.set_horizontal_dir(x, y)
          break
      else:
        continue
      break

    if random.randint(1, 1000) == 1:
      self.direction = random.choice(['up', 'down', 'left', 'right'])

    predict = True
    for i in range(8):
      for j in range(8):
        inital_direction = self.direction
        if not self.is_safe(self.direction, predict):
          if self.direction in ['up', 'down']:
            self.set_horizontal_dir(x, y)
            if self.direction == inital_direction:
              if self.is_safe('right', predict):
                self.direction = 'right'
              else:
                self.direction = 'left'
          else:
            self.set_vertical_dir(x, y)
            if self.direction == inital_direction:
              if self.is_safe('up', predict):
                self.direction = 'up'
              else:
                self.direction = 'down'
          
          if not self.is_safe(self.direction, predict):
            self.set_reverse()

          if not self.is_safe(self.direction, predict):
            all_directions = ['up', 'right', 'down', 'left'] * 2
            for direction in all_directions:
              self.direction = direction
              if self.is_safe(self.direction, predict):
                break
        else:
          break


        # if self.direction == 'down':
        #   if not self.is_safe('down', predict):
        #     self.get_horizontal_dir(x, y)
        # if self.direction == 'left':
        #   if not self.is_safe('left', predict):
        #     self.get_vertical_dir(x, y)
        # if self.direction == 'up':
        #   if not self.is_safe('up', predict):
        #     self.get_horizontal_dir(x, y)
        # if self.direction == 'right':
        #   if not self.is_safe('right', predict):
        #     self.get_vertical_dir(x, y)

        predict = False