#Tic Tac Toe game
#COM 306 Software Engineering
#Noreasters: Craig Haber, Chelsea Vickers, Jacob Nozaki, Tessa Carvalho
#10/30/2020
#A command line interface tool for playing tic tac toe
import random

#initialize global variables
first_turn_player_token = ""
second_turn_player_token = ""
game_over = False
board = ["", "", "", "", "", "", "", "", ""]

#Function to play a single game of tic tac toe
#Args:
#   p1: A String variable of the name of the player who entered their name first
#   p2: A string variable of the name of the player who entered their name first
def play_game(p1, p2):
    first_turn_player, second_turn_player = choose_turn_order(p1, p2)
    #define global variables
    global first_turn_player_token, second_turn_player_token, game_over, board
    choose_token(first_turn_player, second_turn_player)
    cur_player = first_turn_player
    while game_over == False:
        play_turn(cur_player)
        if cur_player == first_turn_player:
            cur_player = second_turn_player
        else:
            cur_player = first_turn_player


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
    #loops through to make sure there is proper input
    while(True):
        move = input(turn_player, " enter an index 1-9 that corresponds to an open spot.")
        #checks if move is a valid input
        if move not in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
            print("That is an invalid input. Try again with a number 1-9.")
        #if empty, the spot will be filled with the proper player token
        elif board[int(move)-1] == "":
            if turn_player == first_turn_player:
                board[int(move)-1] = first_turn_player_token
            else:
                board[int(move)-1] = second_turn_player_token
            break
        #board spot is full
        else:
            print("That spot has already been filled! Try again.")
            
#Function to play a single turn in a game of tic tac toe
#Args:
#   first_turn_player: A string that contains the name of the player that has the first turn
#   second_turn_player: A string that contains the name of the player who has the second turn
#   turn_player: A string that contains the name of the player whose has the current turn
def play_turn(first_turn_player, second_turn_player, turn_player):
    get_next_move(turn_player)
    display_board()
    determine_game_over(first_turn_player, second_turn_player)


#Determine if the game has ended, showing the results and allowing user to restart the game if the game has ended
#Args:
#   first_turn_player: A String variable of the name of the player going first
#   second_turn_player: A string variable of the name of the player going second
def determine_game_over(first_turn_player, second_turn_player):
    #Intialize boolean variables
    is_winner_found = False
    game_has_ended = False
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
        is_token_empty = board[triple[0]] == ""
        if is_all_same_token and (not is_token_empty):
            #Since a player has won, all tokens in the triple are the same, so any token in the triple is the winning token
            winner_token = board[triple[0]]
            #Determine/print the name of the winning player
            if first_turn_player_token == winner_token:
                print("CONGRATULATIONS " + first_turn_player + " YOU WIN!!!\n")
            elif second_turn_player_token == winner_token:
                print("CONGRATULATIONS " + second_turn_player + " YOU WIN!!!\n")
            is_winner_found = True
            game_has_ended = True
            break
    #Check if there's a tie
    if not is_winner_found:
        #Ensure that every space in the board has been filled
        if all([token != "" for token in board]):
            print("THE GAME HAS ENDED, IT IS A TIE.")
            game_has_ended = True

    #End the game
    while game_has_ended:
        #Change global variable of game_over to true
        game_over = True
        #Determine if the player would like to play again
        play_again_choice = input("Would you like to play again (yes/no)?: ")
        if play_again_choice in ["YES", "Yes", "YeS", "YEs", "yES", "yEs", "yeS", "yes", "y", "Y"]:
            play_game(first_turn_player, second_turn_player)
            game_has_ended = False
        elif play_again_choice in ["No", "no", "NO", "nO", "n", "N"]:
            print("\nThanks for playing!")
            game_has_ended = False
        else:
            print("\nThat was not a valid input, please try again.\n")

#Function to run the whole program
def main():
    print_rules()
    p1, p2 = enter_names()
    play_game(p1, p2)

#main()


