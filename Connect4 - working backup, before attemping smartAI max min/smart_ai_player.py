from math import inf 
from game_dimmensions import width, height
from helper_functions import *

# Any integer from 0 to +inf
# The higher it is, the more difficult the SmartAI is (at the cost of longer computation time)
DIFFICULTY = 7 

class SmartAI:
    cache = {}  # stores mappings of a particular board config (game state) to its evaluated value

    @staticmethod
    def find_empty_spaces(board, b_width=width, b_height=height):
        count = 0
        for i in range(b_height):  
            for j in range(b_width):  
                if board[i][j] == "-":
                    count += 1

        return count

    @staticmethod
    def evaluate_curr_pos(board, b_width=width, b_height=height):
        score = 0
        mid_col = b_width // 2  # index of mid col
        # pieces in the cols at + near the middle are more valuable/potent
        for i in range(b_height):
            for j in (mid_col - 1, mid_col, mid_col + 1): 
                if board[i][j] == "X":
                    score += 1
                elif board[i][j] == "O":
                    score -= 1

        # the remaining logic finds and counts the no. of almost winning structures present for both players
        # having an almost winning structure should influence the score more than having pieces at the center
        for row in board:
            for i in range(len(row) - 3):
                r_slice = row[i:i + 4]
                if r_slice.count("X") == 3 and r_slice.count("-") == 1:
                    score += 3
                elif r_slice.count('O') == 3 and r_slice.count("-") == 1:
                    score -= 3

        cols = list(zip(*board))
        for col in cols:
            for i in range(len(col) - 3):
                c_slice = col[i:i + 4]
                if c_slice.count("X") == 3 and c_slice.count("-") == 1:
                    score += 3
                elif c_slice.count('O') == 3 and c_slice.count("-") == 1:
                    score -= 3

        for row_i in range(b_height - 3):
            for col_i in range(b_width - 3):
                desc_diag_window = (board[row_i][col_i], board[row_i + 1][col_i + 1], board[row_i + 2][col_i + 2], board[row_i + 3][col_i + 3])
                if desc_diag_window.count("X") == 3 and desc_diag_window.count("-") == 1:
                    score += 3
                elif desc_diag_window.count('O') == 3 and desc_diag_window.count("-") == 1:
                    score -= 3

        for row_i in range(b_height - 1, b_height - 4, -1):
            for col_i in range(b_width - 3):
                asc_diag_window = (board[row_i][col_i], board[row_i - 1][col_i + 1], board[row_i - 2][col_i + 2], board[row_i - 3][col_i + 3])
                if asc_diag_window.count("X") == 3 and asc_diag_window.count("-") == 1:
                    score += 3
                elif asc_diag_window.count('O') == 3 and asc_diag_window.count("-") == 1:
                    score -= 3

        return score

    @staticmethod
    def minimax(is_max, board, depth, alpha, beta):
        # handling of terminal nodes
        # 1. nodes that result in win/loss/draw
        # 2. nodes that have reached a certain depth (exploring the game tree beyond this depth would take too much time)
        res = check_win(board)
        if res is not None:
            if res == "X":
                return 1 + SmartAI.find_empty_spaces(board)
            else:

                return -1 - SmartAI.find_empty_spaces(board)

        elif depth == DIFFICULTY:
            return SmartAI.evaluate_curr_pos(board)  # additional func to evaluate the curr board state

        elif is_full(board) is True:
            return 0

        if is_max:
            # maximizer plays X in this simulation
            best_value = -inf
            for move in available_moves(board):
                board[move[0]][move[1]] = "X"
                immutable_board = tuple(map(tuple, board))
                if immutable_board in SmartAI.cache:
                    move_value = SmartAI.cache[immutable_board]
                else:
                    move_value = SmartAI.minimax(False, board, depth + 1, alpha, beta)  # each recursive call goes 1 level deeper into the game tree
                    SmartAI.cache[immutable_board] = move_value  # store board into the cache

                board[move[0]][move[1]] = "-"
                best_value = max(best_value, move_value)
                alpha = max(best_value, alpha)
                if alpha >= beta:
                    break

            return best_value

        else:
            # minimizer plays O in this simulation
            best_value = +inf
            for move in available_moves(board):
                board[move[0]][move[1]] = "O"
                immutable_board = tuple(map(tuple, board))
                if immutable_board in SmartAI.cache:
                    move_value = SmartAI.cache[immutable_board]
                else:
                    move_value = SmartAI.minimax(True, board, depth + 1, alpha, beta)  # each recursive call goes 1 level deeper into the game tree
                    SmartAI.cache[immutable_board] = move_value

                board[move[0]][move[1]] = "-"
                best_value = min(best_value, move_value)
                beta = min(best_value, beta)
                if alpha >= beta:
                    break

            return best_value

    @staticmethod
    def make_move(board, _):
        #  SmartAI plays X and is the maximizer
        best_move = (0, 0)
        best_value = -inf

        for move in available_moves(board):
            board[move[0]][move[1]] = "X"
            move_value = SmartAI.minimax(False, board, 0, -inf, +inf)
            board[move[0]][move[1]] = "-"
            if move_value > best_value:
                best_value = move_value
                best_move = move

        return best_move
