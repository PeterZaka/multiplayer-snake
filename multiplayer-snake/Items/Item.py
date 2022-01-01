import random

import sys
sys.path.insert(0, '..')
from Position import Position

class Item:

  def __init__(self, character, field):
    self.character = character
    self.status = 'unactivated'

    open_spots = []
    for i, row in enumerate(field):
      for j, spot in enumerate(row):
        if len(spot) == 1 and spot[0] == ' ': open_spots.append(Position(j, i))
    
    self.pos = random.choice(open_spots)

  def activate(self, snake):
    self.status = 'activated'
    snake.size += 1
    pass