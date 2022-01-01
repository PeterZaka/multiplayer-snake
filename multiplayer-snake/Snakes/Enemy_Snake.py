from Snake import Snake

class Enemy_Snake(Snake):
		def update_controls(self):
				if self.direction == 'down':
						if self.pos.y + 1 == len(self.game.field):
								self.direction = 'left'
				if self.direction == 'left':
						if self.pos.x - 1 == -1:
								self.direction = 'up'
				if self.direction == 'up':
						if self.pos.y - 1 == -1:
								self.direction = 'right'
				if self.direction == 'right':
						if self.pos.x + 1 == len(self.game.field[0]):
								self.direction = 'down'
