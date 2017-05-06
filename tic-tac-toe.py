#Ayomiga
#print "\a"
#print "\n\n"
#print "\a\a\a"

#print "\t\t\t Fancy credits"

#print "\t\t\t \\ \\ \\ \\"
#print "\t\t\t tby"
#print "\t\t\t \\\\\\\\\\"
def instructions():
   # print """
    #""The game instructions""
   print'welcome to the greatest intellectual task of the year \n \t\t\t TIC-TAC-TOE \n'
   print"You will be up againt the greatest challenger of all time _Mrs Silicon Brain_ x515CA \n"
   print"you will make you move known by entering a number mapped to a particular position"
   print"\t\t\t 0 | 1 | 2 "
   print"\t\t\t ---------- "
   print"\t\t\t 3 | 4 | 5 "
   print"\t\t\t ---------- "
   print"\t\t\t 6 | 7 | 8 "
   print"Prepare youself or you'll be beaten shamefully, because it is guaranteed you will still be beaten"
    #"""

def ask(question):
    responce = None
    while responce not in ("y", "n"):
        responce = raw_input(question).lower()
        #this creates an asking loop till the input is in 'y' or 'n'
    return responce

def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(raw_input(question))
    return response

def pieces():
    #who goes first
    go_first = ask("Do you want to take the first move? (y/n): ")
    if go_first =="y":
        print "\n Then take the first move. you will need it :-)"
        human = X
        computer = O
    else:
        print "\n Your bravery will be your undoing ...but i'll go easy on you ;-(=)"
        computer = X
        human = O
    return computer, human

def new_board():
    board = []
    for square in range(num_squares):
        board.append(empty)
    return board

def display_board(board):
    print"\n\t\t\t",board[o], "|", board[1], "|", board[2]
    print"\t\t\t ----------"
    print"\t\t\t",board[3], "|", board[4], "|", board[5]
    print"\t\t\t ----------"
    print"\t\t\t",board[6], "|", board[7], "|", board[8], "\n"

def winner(board):
    ways_to_win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (1, 4, 8), (2, 4, 6))
    for row in ways_to_win:
        if board[row[0]] == board[row[1]] == board[row[2]] !=empty:
            winner = board[row[0]]
            return winner
        if empty not in board:
            return tie
        return None

def human_move(board, human):
    #get the human move
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0-8): ", 0, num_squares)
        if move not in legal:
            print "\nThat square is already occupied, i know you'll lose but make me enjoy it"
        print "Fine..."
        return move

def computer_move(board, computer, human):
    #computer move
    board = board[:]
    #the best positions to have, in order
    best_moves = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print"I shall take square number..."
    
    #if computer can win take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print move
            return move
        # done checking this move, undo it
        board[move] = empty

        #if human can win, block that move
        for move in legal_moves(board):
            board[move] = human
            if winner(board) == human:
                print move
                return move
        #done checking this move, undo it
        board[move] = empty

        #since no one can win on the next move, pick best open square
        for move in best_moves:
            if move in legal_moves(board):
                print move
                return move
            
def next_turn(turn):
    #switch turns
    if turn == X:
        return O
    else:
        return X
    
def congrat_winner(the_winner, computer, human):
    if the_winner != tie:
        print the_winner, "won!\n"
    else:
        print "it's a tie! \n"



#main code
X = "X"
O = "O"
empty = ""
tie = "Tie"
num_squares = 9

print"My name is X515CA"
instructions()
##
answer = ask("Do you want to play this game? \n\t'y' or 'n':")
print"You have chosen ",answer
if(answer == "n"):
    quit()


##main main
versus = raw_input("Do you want to play with another human (versus mode:) or with the computer. \n\t\t press 1 for human and 2 for computer: ")
while versus not in ("1" , "2"):
   versus = raw_input("Do you want to play with another human (versus mode:) or with the computer. \n\t\t press 1 for human and 2 for computer: ")

if (versus == '1' ):
   player2 = raw_input("what is the name of player 2: ")
   while player2 in (" ",""):
      player2 = raw_input("what is the name of player 2:")
                          
                          
                       

else (versus == '2'):
   computer, human = pieces()
   turn = X
   board = new_board()
   display_board(board)

   while not winner(board):
       if turn == human:
           move = human_move(board, human)
           board[move] = human
       else:
           move = computer_move(board, computer, human)
           board[move] = computer
       display_board(board)
       turn = next_turn(turn)

       the_winner = winner(board)
       congrat_winner(the_winner, computer, human)

