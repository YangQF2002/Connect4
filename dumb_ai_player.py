from random import choice
from helper_functions import available_moves

class DumbAI:
    @staticmethod
    def make_move(board):
        move = choice(available_moves(board))
        return move
