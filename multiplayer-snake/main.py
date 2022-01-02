import pygame
import sys
sys.path.insert(0, 'Snakes')
from Player_Snake import Player_Snake
from Enemy_Snake import Enemy_Snake

from Game import Game

if __name__ == '__main__':

		pygame.init()
		pygame.font.init()

		WIDTH = 500
		HEIGHT = 500

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
				screen_settings = (screen, WIDTH, HEIGHT, 15)
				snakes = [Player_Snake('P', 1, 1), Enemy_Snake('E', 18, 1)]
				for i in range(2, 18, 2):
						snakes.append(Enemy_Snake('E', i, i))
				game = Game(snakes, field, screen_settings)
				game.display()
				while(game.status == 'Ongoing'):
						clock.tick(9)

						game.update_controls()
						game.update_movements()
						game.update_field()
						game.update_collisions()
						game.display()
				print(game.status)