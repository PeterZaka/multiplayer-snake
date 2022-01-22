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

  def is_safe(self, x, y, predict):
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
            if y > self.pos.y:
              self.direction = 'down'
            elif y < self.pos.y:
              self.direction = 'up'
            elif x > self.pos.x:
              self.direction = 'right'
            elif x < self.pos.x:
              self.direction = 'left'
          else:
            if x > self.pos.x:
              self.direction = 'right'
            elif x < self.pos.x:
              self.direction = 'left'
            elif y > self.pos.y:
              self.direction = 'down'
            elif y < self.pos.y:
              self.direction = 'up'

    if random.randint(1, 1000) == 1:
      self.direction = random.choice(['up', 'down', 'left', 'right'])

    predict = True
    for i in range(2):
      for j in range(2):
        if self.direction == 'down':
          if not self.is_safe(self.pos.x, self.pos.y + 1, predict):
            self.direction = 'left'
        if self.direction == 'left':
          if not self.is_safe(self.pos.x - 1, self.pos.y, predict):
            self.direction = 'up'
        if self.direction == 'up':
          if not self.is_safe(self.pos.x, self.pos.y - 1, predict):
            self.direction = 'right'
        if self.direction == 'right':
          if not self.is_safe(self.pos.x + 1, self.pos.y, predict):
            self.direction = 'down'

        predict = False