import pygame
import random
import replit
from time import sleep

import sys
sys.path.insert(0, 'multiplayer-snake/Snakes')
from Player_Snake import Player_Snake
from Enemy_Snake import Enemy_Snake

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

    # Random field
    if random.randint(0, 1):
      field = list(field)
      for i in range(1, field_height - 1):
        field[(field_width + 1) * i + random.randint(1, field_width - 2)] = '#'
      field = ''.join(field)

    snakes = [Enemy_Snake('E1', 1, 1)]
    snakes.append(Enemy_Snake('E2', field_width - 2, 1))
    if random.randint(0, 1):
      snakes.append(Enemy_Snake('E3', 1, field_height - 2))
      snakes.append(Enemy_Snake('E4', field_width - 2, field_height - 2))

    game = Game(snakes, field, screen_settings)
    game.display()

    game_counter = 0
    while(game.status == 'Ongoing'):
      game_counter += 1
      if not (pause or unbound): clock.tick(10)

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
      game.update_field()
      game.update_collisions()
      game.display()

      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_p:
            pause = True
          if event.key == pygame.K_u:
            unbound = not unbound

      if pause:
        print()
        print('Press m to show wanted movement')
        print('Press n to advance to next frame')
        print('Press p to unpause')
        key_pressed = waitUntilKey(pygame.K_p, pygame.K_n, pygame.K_m)
        if key_pressed == pygame.K_p:
          print('\nGame unpaused')
          pause = False
        elif key_pressed == pygame.K_m:
          debug_movement = True

      pygame.event.pump()

    print(game_counter)

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
 
    sleep(3)
    # if waitUntilKey(pygame.K_SPACE, pygame.K_u) == pygame.K_u:
    #   unbound = not unbound