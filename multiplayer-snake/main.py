import pygame
import random
import replit
from time import sleep

import sys
sys.path.insert(0, 'multiplayer-snake/Snakes')
from Player_Snake import Player_Snake
from Enemy_Snake import Enemy_Snake
from Tutorial_Snake import my_snake

from Game import Game
from common import *

debug = True

# How to debug:
# Press p to pause the game
# Once paused, you can either press n or m
# n will advance to the next frame
# m will show every snake's next wanted movement in the console
# p will unpause the game

if __name__ == '__main__':
  pygame.init()
  pygame.font.init()

  MAX_SIZE = min([pygame.display.Info().current_h, pygame.display.Info().current_w]) - 25

  SCREEN_WIDTH = MAX_SIZE
  SCREEN_HEIGHT = MAX_SIZE

  field_width = 20
  field_height = 20

  block_size = min([SCREEN_WIDTH, SCREEN_HEIGHT]) / (max([field_width, field_height]) + 2)

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  pause = False
  debug_movement = False
  unbound = False

  while(True):
    field = (' ' * field_width + '|') * field_height
    screen_settings = (screen, SCREEN_WIDTH, SCREEN_HEIGHT, block_size * 0.8, block_size * 0.2)

    snakes = [my_snake('me', 1, 1)]
    snakes.append(Enemy_Snake('E', 18, 1))
    snakes.append(Enemy_Snake('E', 1, 18))
    snakes.append(Enemy_Snake('E', 18, 18))

    # field = list(field)
    # for i in range(1, field_height - 1):
    #   field[(field_width + 1) * i + random.randint(1, field_width - 2)] = '#'
    # field = ''.join(field)

    game = Game(snakes, field, screen_settings)
    game.display()

    while(game.status == 'Ongoing'):
      
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_p:
            pause = True
          elif event.key == pygame.K_u:
            unbound = not unbound
          elif event.key == pygame.K_e:
            for snake in game.snakes:
              snake.status = 'Dead'

      if pause:
        print('\nPress m to show wanted movement')
        print('Press n to advance to next frame')
        print('Press p to unpause')
        key_pressed = waitUntilKey(pygame.K_p, pygame.K_n, pygame.K_m)
        if key_pressed == pygame.K_p:
          print('\nGame unpaused')
          pause = False
        elif key_pressed == pygame.K_m:
          debug_movement = True

      if not (pause or unbound): clock.tick(10)

      game.update_field()
      game.update_controls()
      if debug_movement:
        print()
        for snake in game.snakes:
          if snake.status != 'Dead':
            print(f'{snake.character} {snake.direction}')
        print('Press n to continue')
        waitUntilKey(pygame.K_n)
        debug_movement = False

      game.update_movements()
      game.update_collisions()
      game.display()

      pygame.event.pump()

    if game.status == 'Tie' or len(snakes) == 1:
      text_color = (0, 0, 0)
      back_color = (255, 255, 255)
    else:
      statuses = [snake.status for snake in snakes]
      text_color = snakes[statuses.index('Alive')].tail_color
      back_color = []
      for color in text_color:
        back_color.append(max(0, 255 - color))

    font = pygame.font.SysFont('Comic Sans MS', SCREEN_WIDTH // 10)

    text = font.render(game.status, True, back_color, text_color)
 
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT * 4 // 5)

    screen.blit(text, textRect)
    pygame.display.update()
 
    key_pressed = waitUntilKey(pygame.K_SPACE, pygame.K_u, pygame.K_p)
    if key_pressed == pygame.K_u:
      unbound = not unbound
    elif key_pressed == pygame.K_p:
      pause = not pause