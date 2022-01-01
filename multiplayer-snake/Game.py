import copy

import sys
sys.path.insert(0, 'Items')
from Item import Item

class Game:

		def __init__(self, snakes, field):
				self.snakes = snakes
				self.status = 'Ongoing'

				self.empty_field = []
				self.field = []
				row = []
				for c in field:
						if c != '|':
								for snake in snakes:
										if c == snake.character:
												snake.set_pos(len(row), len(self.empty_field))
												row.append([' '])
												break
								else:
										row.append([c])
						else:
								self.empty_field.append(row)
								row = []

				self.items = []
				self.update_field()

				self.items = [Item('A', self.field)]
				self.update_field()

				for snake in snakes:
						snake.set_game(self)

		def update_controls(self):
				for snake in self.snakes:
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
								self.field[snake.pos.y][snake.pos.x].append(snake.character)
						for piece in snake.body:
								self.field[piece.y][piece.x].append(snake.character.lower())

		def display(self):
				field = [[spot[-1] for spot in row] for row in self.field]

				for row in field:
						print('|' + ''.join(row) + '|')
