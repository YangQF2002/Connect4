from helper_functions import available_moves

class Human:
    @staticmethod
    def make_move(board, filled_squares):
        while True:
            temp = input("Enter your move in the format: row,col ").strip().split(",")
            try:
                temp_1 = tuple(map(int, temp))
            except ValueError as error_msg:
                print(error_msg)
                continue
            else:
                move = tuple(map((lambda item: item - 1), temp_1))
                if move not in available_moves(board):
                    if move in filled_squares: 
                        print("This move is not possible! The square is already taken! ")
                    else: 
                        print("This move is not possible! Remember to fill each column from the bottom! ")
                    
                else:
                    return move
