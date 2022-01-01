from Snake import Snake

class Player_Snake(Snake):
		def update_controls(self):
				dir = input()
				if dir == 'w':
						self.direction = 'up'
				elif dir == 'a':
						self.direction = 'left'
				elif dir == 's':
						self.direction = 'down'
				elif dir == 'd':
						self.direction = 'right'