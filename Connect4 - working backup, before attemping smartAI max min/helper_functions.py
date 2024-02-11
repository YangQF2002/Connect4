from game_dimmensions import width, height 

def create_board(b_width=width, b_height=height):
    board = []
    for _ in range(b_height):  
        l_each_row = []
        for _ in range(b_width):  
            l_each_row.append("-")
        board.append(l_each_row)
    return board


def display_board(board):
    for item in board:
        print(item, end='\n')


def check_win(board, b_width=width, b_height=height):
    for row in board:
        for i in range(len(row) - 3):
            if len(set(row[i:i + 4])) == 1 and row[i] != "-":  # getting a 4-unit slice from each row item
                if row[i] == "X":
                    return "X"
                else:
                    return "O"

    cols = list(zip(*board))
    for col in cols:
        for i in range(len(col) - 3):
            if len(set(col[i:i + 4])) == 1 and col[i] != "-":  # getting a 4-unit slice from each col item
                if col[i] == "X":
                    return "X"
                else:
                    return "O"

    # desc diagonal check
    for row_i in range(b_height - 3):
        for col_i in range(b_width - 3):
            if board[row_i][col_i] == board[row_i + 1][col_i + 1] == board[row_i + 2][col_i + 2] == board[row_i + 3][col_i + 3] and board[row_i][col_i] != "-":
                if board[row_i][col_i] == "X":
                    return "X"
                else:
                    return "O"

    # asc diagonal check
    for row_i in range(b_height - 1, b_height - 4, -1):
        for item_i in range(b_width - 3):
            if board[row_i][col_i] == board[row_i - 1][col_i + 1] == board[row_i - 2][col_i + 2] == board[row_i - 3][col_i + 3] and board[row_i][col_i] != "-":
                if board[row_i][col_i] == "X":
                    return "X"
                else:
                    return "O"


def available_moves(board):
    # search each col, starting from the bottom
    # each col can have at most 1 move
    # once an empty space is detected, stop searching that col and move onto the next

    cols = list(zip(*board))
    l_available_moves = []
    for col_i, col in enumerate(cols):  
        for i in range(len(col) - 1, -1, -1):  
            if col[i] == "-":
                l_available_moves.append((i, col_i))
                break

    return l_available_moves

def is_full(board):
    res = available_moves(board)
    if len(res) == 0:
        return True
    else:
        return False







