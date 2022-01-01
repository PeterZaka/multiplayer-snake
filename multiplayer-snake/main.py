import sys
sys.path.insert(0, 'Snakes')
from Player_Snake import Player_Snake
from Enemy_Snake import Enemy_Snake

from Game import Game

if __name__ == '__main__':

# |          |
# | P      E |
# |          |
# |          |
# |          |

		while(True):
				field = "          | P      E |          |          |          |"
				game = Game([Player_Snake('P'), Enemy_Snake('E')], field)
				game.display()
				while(game.status == 'Ongoing'):
						game.update_controls()
						game.update_movements()
						game.update_field()
						game.update_collisions()
						game.display()
				print(game.status)