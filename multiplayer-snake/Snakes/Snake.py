import sys
sys.path.insert(0, '..')
from Position import Position

class Snake:

		ID = 0

		def __init__(self, character, x, y):
				self.character = character
				self.set_pos(x, y)
				self.direction = 'down'
				self.size = 3
				self.body = []

				self.status = 'Alive'
				self.set_color((0, 0, 255), (0, 0, 255))

				self.ID = Snake.ID
				Snake.ID += 2

				self.init()

		def set_pos(self, x, y):
				self.pos = Position(x, y)

		def set_game(self, game):
				self.game = game

		def set_color(self, head_color, tail_color):
						self.head_color = head_color
						self.tail_color = tail_color

		def init(self):
				pass

		def update_controls(self):
				pass

		def update_movement(self):
				if self.status == 'Dead': return

				if len(self.body) < self.size: self.body.append(self.pos.copy())
				self.body.pop(-1)
				self.body.insert(0, self.pos.copy())

				if self.direction == 'down':
						self.pos.y += 1
				elif self.direction == 'up':
						self.pos.y -= 1
				elif self.direction == 'right':
						self.pos.x += 1
				elif self.direction == 'left':
						self.pos.x -= 1

		def update_collision(self):
				if self.status == 'Dead': return

				if (self.pos.y < 0 or self.pos.y >= len(self.game.field) or
								self.pos.x < 0 or self.pos.x >= len(self.game.field[0])):
						self.status = 'Dead'
						return

				spot = self.game.field[self.pos.y][self.pos.x]
				chosen_item = [item for item in self.game.items if item.character == spot[1]]

				if len(chosen_item) != 0:
						chosen_item[0].activate(self)

				if len(spot) > 2:
						if len(chosen_item) == 0 or len(spot) > 3:
								self.status = 'Dead'
						return