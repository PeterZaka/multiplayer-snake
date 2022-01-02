import copy
import pygame

import sys
sys.path.insert(0, 'Items')
from Item import Item

class Game:

		def __init__(self, snakes, field, screen_settings):
				self.snakes = snakes
				self.status = 'Ongoing'

				self.empty_field = []
				self.field = []
				row = []
				for c in field:
						if c != '|':
										row.append([c])
						else:
								self.empty_field.append(row)
								row = []

				self.FIELD_WIDTH = len(self.empty_field[0])
				self.FIELD_HEIGHT = len(self.empty_field)

				self.items = []
				self.update_field()

				self.items = [Item('A', self.field)]
				self.update_field()

				for snake in snakes:
						snake.set_game(self)

				self.screen, self.WIDTH, self.HEIGHT, self.BLOCK_SIZE = screen_settings

		def update_controls(self):
				for snake in self.snakes:
						if snake.status != 'Dead':
								snake.update_controls();

		def update_movements(self):
				for snake in self.snakes:
						snake.update_movement();

		def update_collisions(self):
				for snake in self.snakes:
						snake.update_collision()

				for item in self.items:
						if item.status == 'activated':
								self.items.remove(item)
								self.items.append(Item('A', self.field))

				statuses = [snake.status for snake in self.snakes]

				if statuses.count('Dead') == len(statuses):
						self.status = 'Tie'

				if statuses.count('Dead') == len(statuses) - 1:
						self.status = self.snakes[statuses.index('Alive')].character + ' won'

		def update_field(self):
				self.field = copy.deepcopy(self.empty_field)

				for item in self.items:
						self.field[item.pos.y][item.pos.x].append(item.character)

				for snake in self.snakes:
						if not (snake.pos.y < 0 or snake.pos.y >= len(self.empty_field) or
														snake.pos.x < 0 or snake.pos.x >= len(self.empty_field[0])):
								if snake.status == 'Dead':
										self.field[snake.pos.y][snake.pos.x].append('#')
								else:
										self.field[snake.pos.y][snake.pos.x].append(snake.ID)
						for piece in snake.body:
								if snake.status == 'Dead':
										self.field[piece.y][piece.x].append('#')
								else:
										self.field[piece.y][piece.x].append(snake.ID + 1)

		def display(self):
				#field = [[spot[-1] for spot in row] for row in self.field]
				#for row in field:
				#		print('|' + ''.join([str(i) for i in row]) + '|')
				#print()

				self.screen.fill((0, 0, 0))

				BLOCK_SIZE = self.BLOCK_SIZE
				top = self.HEIGHT - 10 - self.FIELD_HEIGHT * (BLOCK_SIZE + 5)
				pygame.draw.rect(self.screen, (0, 255, 0), (10, top, self.FIELD_WIDTH * (BLOCK_SIZE + 5), self.FIELD_HEIGHT * (BLOCK_SIZE + 5)))

				for item in self.items:
						x, y = 10 + item.pos.x * (BLOCK_SIZE + 5), top + item.pos.y * (BLOCK_SIZE + 5)
						pygame.draw.rect(self.screen, item.color, (x, y, BLOCK_SIZE, BLOCK_SIZE))

				for snake in self.snakes:
						x, y = 10 + snake.pos.x * (BLOCK_SIZE + 5), top + snake.pos.y * (BLOCK_SIZE + 5)
						pygame.draw.rect(self.screen, snake.head_color, (x, y, BLOCK_SIZE, BLOCK_SIZE))
						for part in snake.body:
								x, y = 10 + part.x * (BLOCK_SIZE + 5), top + part.y * (BLOCK_SIZE + 5)
								pygame.draw.rect(self.screen, snake.tail_color, (x, y, BLOCK_SIZE, BLOCK_SIZE))

				pygame.display.flip()

#				for row in field:
#						print('|' + ''.join(row) + '|')