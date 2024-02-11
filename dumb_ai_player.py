from random import choice
from helper_functions import available_moves

class DumbAI:
    def make_move(self, board):
        move = choice(available_moves(board))
        return move
