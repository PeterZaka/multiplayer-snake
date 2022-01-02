from Snake import Snake
import pygame

class Player_Snake(Snake):
  def init(self):
    self.set_color((0, 177, 255), (100, 0, 255))

  def update_controls(self):
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          self.direction = 'right'
        if event.key == pygame.K_LEFT:
          self.direction = 'left'
        if event.key == pygame.K_UP:
          self.direction = 'up'
        if event.key == pygame.K_DOWN:
          self.direction = 'down'