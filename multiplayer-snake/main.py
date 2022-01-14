import pygame
import random

import sys
sys.path.insert(0, 'Snakes')
from Player_Snake import Player_Snake
from Enemy_Snake import Enemy_Snake
from Enemy_Snake2 import Enemy_Snake2

from Game import Game

if __name__ == '__main__':
  pygame.init()
  pygame.font.init()

  WIDTH = 35*22
  HEIGHT = 35*22

  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  clock = pygame.time.Clock()

# |          |
# | P      E |
# |          |
# |          |
# |          |

  while(True):
    width = 20
    height = 20
    field = (' ' * width + '|') * height
    screen_settings = (screen, WIDTH, HEIGHT, 30, 5)

    snakes = [Enemy_Snake('E', 1, 1), Enemy_Snake2('E', 2, 1), Enemy_Snake('E', 17, 1), Enemy_Snake2('E', 18, 1)]
    if random.randint(1,2) == 1:
      snakes = [snakes[0], snakes[-1]]

    game = Game(snakes, field, screen_settings)
    game.display()
    while(game.status == 'Ongoing'):
      clock.tick(10)

      game.update_controls()
      game.update_movements()
      game.update_field()
      game.update_collisions()
      game.display()

      pygame.event.pump()
    print(game.status)