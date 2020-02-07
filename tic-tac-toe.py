from array import *
import time

board = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
board_coords = {"7": (0, 0), "8": (0, 1), "9": (0, 2), "4": (1, 0),
           "5": (1, 1), "6": (1, 2), "1": (2, 0), "2": (2, 1), "3": (2, 2)}
player1_score = 0
player2_score = 0
whos_turn = 1
player1_shape = "X"
player2_shape = "O"
winner_declared = False

# ------------------- Board functions ------------------- # 
def display_board(board):
    '''
    Displays the board in the console
    '''
    
    print("\n" * 100)
    col = " " * 7
    vertical_lines = (" " * 3) + col + " | " + col + " | " + col
    horizontal_line = (" " * 2) + "-" * 29
    
    for row in range(0, 3):
        for column in range(0,3):        
            if column == 1:
                firstRow = "  " + (" " * 4) + "{col1}".format(col1=str(board[row][0])) + " " * 3 + " | " + (
                    " " * 3) + "{col2}".format(col2=str(board[row][1])) + " " * 3 + " | " + (" " * 3) + "{col3}".format(col3=str(board[row][2])) + " " * 3
                print(firstRow)
            else:
                print(vertical_lines)

        if row < 2:
            print(horizontal_line)

def reset_board():
    global board
    '''
    Resets the board to being empty
    '''
    
    for i in range(0, 3):
        for val in range(0, 3):
            board[i][val] = " "

def show_example_board():
    '''
    If a player makes an invalid move, show them the board with the valid keys 
    '''
    
    board = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    display_board(board)

# ------------------- End board functions ------------------- # 

# ------------------- Player interaction ------------------- # 
def determine_player():
    '''
    Find out which player will be X and which will by O
    '''
    
    global player1_shape, player2_shape, whos_turn
    temp_var = input(
        "\nPlayer 1, do you want to be 'X' or 'O' (X goes first)? ")

    while (str(temp_var).lower() != "x" and str(temp_var).lower() != "o"):
        temp_var = input(
            "\nYou typed: {}, you need to type either 'X' or 'O' ".format(temp_var))
        if (temp_var.lower() == "x" or temp_var.lower() == "o"):
            break

    player1_shape = temp_var.upper()
    player2_shape = "O" if player1_shape == "X" else "X"
    whos_turn = 1 if player1_shape == "X" else 2

    print("\nPlayer 1 is: {}\nPlayer 2 is: {}".format(
        player1_shape, player2_shape))
    time.sleep(2)


def replay():
    '''
    Called when a winner has been declared.
    '''
    
    global winner_declared
    
    winner_declared = True
    print("\n\nCONGRATULATIONS PLAYER {} YOU WIN!!!\n\nBelow you can see the current score:\nPlayer 1 wins:\t {} \nPlayer 2 wins:\t {} ".format(whos_turn, player1_score, player2_score))
    return play_again()

def ask_for_restart():
    '''
    Asks if player wants to play again when there are no more moves available 
    '''
    
    print("\n\nLooks like there are no more possible moves.")
    return play_again()
    
def play_again():
    global whos_turn
    
    dont_end_game = input("\nDo you want to play again? (y/n) ")
    while dont_end_game.lower() != "y" and dont_end_game.lower() != "n":
        dont_end_game = input("That's not a valid option, please enter 'y' or 'n'")

        if dont_end_game == "y" or dont_end_game == "n":
            break

    play_again = True if dont_end_game == "y" else False
    
    if play_again: 
        whos_turn = 1 if player1_shape == "X" else 2
        reset_board()
        display_board(board)
        
    return play_again
# ------------------- End player interaction ------------------- # 

# ------------------- Check win ------------------- # 

def check_win(board, move):
    '''
    Called by make_move() to determine if a player has won the game
    '''
    global whos_turn, player1_score, player2_score
    
    move_on_board = board_coords[move]
    
    victory = check_horizontal(board, move)
    
    if not victory:
        victory = check_vertical(board, move)
    
    if not victory and move in "13579":
        victory = check_diagonal(board, move)
    
    if victory:
        if whos_turn == 1:
            player1_score += 1
        else:
            player2_score += 1
            
        return replay()
    else:
        return True

def check_horizontal(board, move):
    '''
    Checks if player has won horizontally 
    '''
    
    move = int(move)
    
    if move >= 7 and move <= 9:
        if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
            return True
        return False

    elif move >= 4 and move <= 6:
        if board[1][0] == board[1][1] and board[1][0] == board[1][2]:
            return True
        return False
    
    else:
        if board[2][0] == board[2][1] and board[2][0] == board[2][2]:
            return True
        return False
    
def check_vertical(board, move):
    '''
    Checks if player has won vertically 
    '''
    
    move = int(move)
    if move in [7,4,1]:
        if board[0][0] == board[1][0] and board[0][0] == board[2][0]:
            return True
        return False

    elif move in [8,5,2]:
        if board[0][1] == board[1][1] and board[0][1] == board[2][1]:
            return True
        return False
    
    else:
        if board[0][2] == board[1][2] and board[0][2] == board[2][2]:
            return True
        return False

def check_diagonal(board, move):
    '''
    Checks if player has won diagonally 
    '''
    
    move = int(move)
    
    if move in [7,5,3]:
        if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
            return True
        return False
   
    else:
        if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
            return True
        return False
# ------------------- End check win ------------------- #    
    
# ------------------- Make moves ------------------- # 

def make_move(move, shape):
    '''
    Replaces the empty space in the board with the current player's shape and calls check_win()
    '''
    
    global board
    my_tuple = board_coords[move]

    valid = board[my_tuple[0]][my_tuple[1]] not in "XO"

    while not valid:
        new_move = input(
            "That spot has already been selected. Make another move: ")
        my_tuple = board_coords[new_move]
        valid = board[my_tuple[0]][my_tuple[1]] not in "XO"

        if valid:
            break

    board[my_tuple[0]][my_tuple[1]] = shape
    display_board(board)
    
    return check_win(board, move)

def get_next_move():
    '''
    Gets player input and calls the make_move function
    '''
    
    global player1_shape, player2_shape, whos_turn, board
    
    spaces_available = check_spaces()
        
    if not spaces_available:
        return ask_for_restart()

    if whos_turn == 1:
        player1_move = input("Player 1's move: ")
        while str(player1_move) not in "123456789" or len(str(player1_move)) != 1:
            show_example_board(board)
            player1_move = input(
                "\nSee above for valid keys to press. Please choose another space: ")
            if str(player1_move) in "123456789" and len(str(player1_move)) == 1:
                break

        continue_playing = make_move(player1_move, player1_shape)
        if not winner_declared:
            whos_turn = 2
    else:
        player2_move = input("Player 2's move: ")
        while str(player2_move) not in "123456789" or len(str(player2_move)) != 1:
            show_example_board(board)
            player2_move = input(
                "\nSee above for valid keys to press. Please choose another space: ")
            if str(player2_move) in "123456789" and len(str(player2_move)) == 1:
                break

        continue_playing = make_move(player2_move, player2_shape)
        if not winner_declared:
            whos_turn = 1
    return continue_playing

# ------------------- End make moves ------------------- #

# ------------------- Start game logic ------------------- # 

def check_spaces():
    '''
    Checks if any more moves can be made
    '''
    space = False
    for row in board:
        if " " in row:
            space = True
            break
             
    return space
    
def start_game():
    '''
    Starts the game
    '''

    global winner_declared
    
    print(("\n" * 50) + "WELCOME TO AUSTIN'S TIC-TAC-TOE!\n")
    time.sleep(1.5)
    
    display_board(board)
    print("Above you can see which keypad number will select which cell on the board:")
    time.sleep(2)

    determine_player()
    reset_board()

    print("\nTIME TO PLAY!\n")
    display_board(board)

    dont_end_game = True

    while(dont_end_game):
        winner_declared = False
        dont_end_game = get_next_move()


def main():
    start_game()

# ------------------- End game logic ------------------- # 

if __name__ == "__main__":
    main()

