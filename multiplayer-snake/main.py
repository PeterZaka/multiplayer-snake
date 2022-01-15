import pygame
import random
import replit

import sys
sys.path.insert(0, 'multiplayer-snake/Snakes')
from Player_Snake import Player_Snake
from Enemy_Snake import Enemy_Snake

from Game import Game

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

  SCREEN_WIDTH = 200
  SCREEN_HEIGHT = 200

  field_width = 20
  field_height = 20

  block_size = min([SCREEN_WIDTH, SCREEN_HEIGHT]) / (max([field_width, field_height]) + 2)

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  pause = False
  debug_movement = False

  while(True):
    field = (' ' * field_width + '|') * field_height
    screen_settings = (screen, SCREEN_WIDTH, SCREEN_HEIGHT, block_size * 0.8, block_size * 0.2)

    snakes = [Enemy_Snake('E1', 1, 1), Enemy_Snake('E2', 18, 1)]

    game = Game(snakes, field, screen_settings)
    game.display()
    while(game.status == 'Ongoing'):
      clock.tick(10)

      game.update_controls()
      if debug_movement:
        print()
        for snake in game.snakes:
          print(f'{snake.character} {snake.direction}')
        print('Press n to continue')
        while(True):
          for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_n:
                debug_movement = False
                break
          else:
            continue
          break

      game.update_movements()
      game.update_field()
      game.update_collisions()
      game.display()

      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_p:
            pause = True

      if pause:
        replit.clear()
        print('Press m to show wanted movement')
        print('Press n to advance to next frame')
        print('Press p to unpause')
        while(True):
          for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_p:
                pause = False
                break
              if event.key == pygame.K_n:
                break
              if event.key == pygame.K_m:
                debug_movement = True
                break
          else:
            continue
          break

      pygame.event.pump()

    font = pygame.font.SysFont('Comic Sans MS', SCREEN_WIDTH // 10)
    text = font.render(game.status, True, (255, 255, 255), (0, 0, 0))
 
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT * 4 // 5)

    screen.blit(text, textRect)
    pygame.display.update()
 
    while(True):
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            break
      else:
        continue
      break