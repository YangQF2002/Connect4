from helper_functions import *
from human_player import Human 
from smart_ai_player import SmartAI 

def play_game(board, x_player, o_player):
    curr_letter = "X"
    filled_squares = []
    while is_full(board) is False:
        print(f'{curr_letter}\'s turn to move! ')
        if curr_letter == "X":
            move = x_player.make_move(board, filled_squares)
        else:
            move = o_player.make_move(board, filled_squares)

        board[move[0]][move[1]] = curr_letter  # move is structured as a two-item tuple
        filled_squares.append(move)
        
        display_board(board)
        res = check_win(board)

        if res is not None:
            print(f'{res} player wins!')
            if res == "X":
                return "X"
            else:
                return "O"

        curr_letter = "O" if curr_letter == "X" else "X"        

    else:
        print("Draw")

def play_again():
    while True:
        user_choice = input("Y to play again, N to quit").upper().strip()
        match user_choice:
            case "N":
                exit()
            case "Y":
                break
            case _:
                print("Invalid input, try again")
                continue

def main():
    x_win_count = 0
    o_win_count = 0
    x_player = SmartAI  # SmartAI can only play X
    o_player = Human

    while True:
        board = create_board()
        res = play_game(board, x_player, o_player)
        match res:
            case "X":
                x_win_count += 1
            case "O":
                o_win_count += 1

        print(f'X has {x_win_count} wins!')
        print(f'O has {o_win_count} wins!')
        play_again()


if __name__ == '__main__':
    main()
