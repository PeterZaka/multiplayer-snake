import pygame

def waitUntilKey(*args):
  while(True):
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key in args:
          return event.key