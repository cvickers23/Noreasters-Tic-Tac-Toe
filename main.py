#Tic Tac Toe game
#COM 306 Software Engineering
#Noreasters: Craig Haber, Chelsea Vickers, Jacob Nozaki, Tessa Carvalho
#10/30/2020
#A command line interface tool for playing tic tac toe
import random
import logging
import logging.handlers
import os

#create a logging object
log = logging.getLogger("script-logger")
#config the log to level of info and so that a timestamp is printed before each log
logging.basicConfig( format='%(asctime)s %(message)s', level=os.environ.get("LOGLEVEL", "INFO"), datefmt = '%Y:%m:%d:%H:%M:%S')
#config logs to be sent to a file
handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE", "game_log.log"))
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
log.addHandler(handler)

#Function to print the rules of Tic Tac Toe
def print_rules():
    print("""Rules of the game:
1. The game is played on a 3x3 square grid.
2. One player's token is X and the other player's token is O.
3. Players take turns putting their token in empty squares in the grid.
4. The first player to get 3 of their tokens in a row (up, down, across, or diagonally) is the winner.
5. When all 9 squares of the grid are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

Example Game Board (with Indices):
1 | 2 | 3
-----------
4 | 5 | 6
-----------
7 | 8 | 9 """)


#Function to play a single game of tic tac toe
#Args:
#   p1: A String variable of the name of the player who entered their name first
#   p2: A string variable of the name of the player who entered their name first
def play_game(p1, p2):
    #load global variables
    global first_turn_player
    global second_turn_player
    first_turn_player, second_turn_player = choose_turn_order(p1, p2)
    choose_token(input_token())
    cur_player = first_turn_player
    while game_over == False:
        play_turn(cur_player)
        if cur_player == first_turn_player:
            cur_player = second_turn_player
        else:
            cur_player = first_turn_player
    ask_play_again()


#Function to allow players to input their names through the command line
#Returns:
#   The two player name strings p1 and p2
def enter_names():
    #accept input of two separate player names
    p1 = input("Enter name of player 1: ")
    p2 = input("Enter name of player 2: ")
    return(p1, p2)


#Function to determine which player goes first
#Args:
#   p1: A String variable of the name of the player who entered their name first
#   p2: A string variable of the name of the player who entered their name first
#Returns:
#   The two player name strings in the order of their randomly chosen turn order (player going first, player going second)
def choose_turn_order(p1, p2):
    players = [p1, p2]
    #Randomly choose player to go first (50/50 odds)
    first_turn = random.choice(players)
    if (first_turn == p1):
        print(p1, " has been randomly chosen to go first")
        return p1, p2
    else:
        print(p2, " has been randomly chosen to go first")
        return p2, p1


#Function to get the next move from the player whose turn it is and add it to the board
#Args:
#   turn_player: A string that contains the name of the player that has the current turn
def get_next_move(turn_player):
    #load global variables
    global board
    #loops through to make sure there is proper input
    while(True):
        move = input(turn_player + " enter an index 1-9 that corresponds to an open spot: ")
         #checks if move is a valid input
        if move not in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            print("That is an invalid input. Try again with a number 1-9.")
        #if empty, the spot will be filled with the proper player token
        elif board[int(move)-1] == " ":
            if turn_player == first_turn_player:
                board[int(move)-1] = first_turn_player_token
                log.info(first_turn_player + " placed an " + first_turn_player_token + " in spot " + move)
            else:
                board[int(move)-1] = second_turn_player_token
                log.info(second_turn_player + " placed an " + second_turn_player_token + " in spot " + move)
            break
        #board spot is full
        else:
            print("That spot has already been filled! Try again.")

            
#Function to play a single turn in a game of tic tac toe
#Args:
#   turn_player: A string that contains the name of the player whose has the current turn
def play_turn(turn_player):
    get_next_move(turn_player)
    display_board()
    determine_game_over()


#Determine if the game has ended, showing the results and allowing user to restart the game if the game has ended
#Args:
#   first_turn_player: A String variable of the name of the player going first
#   second_turn_player: A string variable of the name of the player going second
def determine_game_over():
    global game_over
    #Indices 0-2 are for first row, 3-5 are for second row, 6-8 are for third row
    win_state_indices = [
        #row win state indicies
        [0,1,2],
        [3,4,5],
        [6,7,8],
        #column win state indices
        [0,3,6],
        [1,4,7],
        [2,5,8],
        #diagonal win state indices
        [0,4,8],
        [2,4,6]
    ]
    for triple in win_state_indices:
        is_all_same_token = board[triple[0]] == board[triple[1]] == board[triple[2]]
        is_token_empty = board[triple[0]] == " "
        if is_all_same_token and (not is_token_empty):
            #Since a player has won, all tokens in the triple are the same, so any token in the triple is the winning token
            winner_token = board[triple[0]]
            #Determine/print the name of the winning player
            if first_turn_player_token == winner_token:
                print("CONGRATULATIONS " + first_turn_player + " YOU WIN!!!\n")
            elif second_turn_player_token == winner_token:
                print("CONGRATULATIONS " + second_turn_player + " YOU WIN!!!\n")
            game_over = True
            break
    #Check if there's a tie
    if not game_over:
        #Ensure that every space in the board has been filled
        if all([token != " " for token in board]):
            print("THE GAME HAS ENDED, IT IS A TIE.")
            game_over = True        


#Function to determine if the players want to play again
def ask_play_again():
    global board
    global game_over
    while True:
        #Determine if the players would like to play again
        play_again_choice = input("Would you like to play again (yes/no)?: ")
        if play_again_choice in ["YES", "Yes", "YeS", "YEs", "yES", "yEs", "yeS", "yes", "y", "Y"]:
            board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            game_over = False
            play_game(first_turn_player, second_turn_player)
            break
        elif play_again_choice in ["No", "no", "NO", "nO", "n", "N"]:
            print("\nThanks for playing!")
            break
        else:
            print("\nThat was not a valid input, please try again.\n")

#Function to get user input of token to make testing easier
#returns: the user input of token.
def input_token():
    return input(first_turn_player + ", enter your choice of token (X/x or O/o): ")


#Function to let the first turn player choose their game token, and assigns other token to other player
#Args:
#   first_turn_player: A string containing the name of the player going first
#   second_turn_player: A string containing the name of the player going second
#   token: String of token that user inputted
def choose_token(token):
    #load global variables
    global first_turn_player_token
    global second_turn_player_token
    while(True):
        if (token == "X" or token == "x"): # First turn player entered X/x
            first_turn_player_token, second_turn_player_token = "X", "O" # First turn player gets X, second gets O
            break # Tokens assigned, end loop

        elif (token == "O" or token == "o"): # First turn player entered O/o
            first_turn_player_token, second_turn_player_token = "O", "X" # First turn player gets O, second gets X
            break # Tokens assigned, end loop

        else: # First turn player entered invalid input
            print("Please enter either X/x or O/o.")
            token = input_token()

    # Display assigned tokens
    print(first_turn_player + " is " + first_turn_player_token + ", " +
          second_turn_player + " is " + second_turn_player_token + ".")


#Function to display the current game board
def display_board():
    print("  " + board[0] + "  |  " + board[1] + "  |  " + board[2]) # Row 1
    print("----------------")
    print("  " + board[3] + "  |  " + board[4] + "  |  " + board[5]) # Row 2
    print("----------------")
    print("  " + board[6] + "  |  " + board[7] + "  |  " + board[8]) # Row 3


#Function to run the whole program
def main():
    #initialize global variables
    global first_turn_player, first_turn_player_token, second_turn_player, second_turn_player_token, game_over, board
    first_turn_player = ""
    first_turn_player_token = ""
    second_turn_player = ""
    second_turn_player_token = ""
    game_over = False
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    print_rules()
    p1, p2 = enter_names()
    play_game(p1, p2)

if __name__ == "__main__":
    main()


