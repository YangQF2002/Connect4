from helper_functions import *
from human_player import Human 
from smart_ai_player import SmartAI 
from dumb_ai_player import DumbAI

# at some point, create an interface for this game (ie: using pygame or something)
def select_piece(): 
    while True: 
        player_piece = input("Play as X or O? X goes first! ").upper().strip()
        match player_piece: 
            case "X":
                ai_piece = "O"
                return (player_piece, ai_piece)
            case "O": 
                ai_piece = "X"
                return (player_piece, ai_piece)
            case _: 
                print("Invalid input, try again")
                continue 


def select_ai():
    while True: 
        temp = int(input("Type 1 for SmartAI, type 2 for DumbAI ").strip()) 
        match temp:
            case 1:
                ai_player = SmartAI 
                return ai_player
            case 2: 
                ai_player = DumbAI 
                return ai_player 
            case _:
                print("Invalid input, try again")
                continue 

        
def play_game(board):
    pieces_chosen = select_piece()
    player_piece = pieces_chosen[0]
    ai_piece = pieces_chosen[1]

    ai_class = select_ai()
    human_player = Human() 
    ai_player = ai_class()

    # if player starts first, show them the board initially so they can make the first move 
    if player_piece == "X":
        display_board(board)

    # X starts first 
    curr_letter = "X"
    filled_squares = []
    while is_full(board) is False:
        print(f'{curr_letter}\'s turn to move! ')
        if curr_letter == player_piece:
            move = human_player.make_move(board, filled_squares)
        else:
            # curr_letter == ai_piece
            if ai_class == SmartAI: 
                move = ai_player.make_move(board, ai_piece) 
            else:
                move = ai_player.make_move(board) 

        board[move[0]][move[1]] = curr_letter  # move is structured as a two-item tuple
        filled_squares.append(move)
        
        display_board(board)
        res = check_win(board)

        if res is not None:
            print(f'{res} player wins!')
            if player_piece == res:
                return 0
            else:
                # ai_piece == res 
                if ai_class == SmartAI: 
                    return 1
                else: 
                    return 2 

        curr_letter = "O" if curr_letter == "X" else "X"        

    else:
        print("Draw")


def play_again():
    while True:
        user_choice = input("Y to play again, N to quit ").upper().strip()
        match user_choice:
            case "N":
                exit()
            case "Y":
                break
            case _:
                print("Invalid input, try again")
                continue


def main():
    player_win_count = 0
    smart_ai_win_count = 0
    dumb_ai_win_count = 0 

    while True:
        board = create_board()
        res = play_game(board)
        match res:
            case 0:
                player_win_count += 1
            case 1:
                smart_ai_win_count += 1
            case 2: 
                dumb_ai_win_count += 1

        print(f'Player has {player_win_count} wins!')
        print(f'SmartAI has {smart_ai_win_count} wins!')
        print(f'DumbAI has {dumb_ai_win_count} wins!')
        play_again()

if __name__ == '__main__':
    main()
