# Simple tic-tac-toe game 
# Created by Habib Ali

# The board functions that create the board are created by John Halloran with my comments 
# Main function is ran to start the game

# The board is displayed and runs the function Player_1
def main():
    boardsize = 3                          #This sets the dimensions of the board so it is 3 by 3
    board = defineBoard(boardsize)
    createBoardLabels(board, boardsize)
    drawBoard(board, boardsize)
    Player_1(board, boardsize)

# Draws the basic version of the board with no grid
def defineBoard(boardsize):
    board = [[""] * boardsize for i in range(boardsize)]        
    return board

# Make the counters needed for the board the counters are numbers
def createBoardLabels(board, boardsize):                       
    counter = 0
    for i in range(boardsize):
        for j in range(boardsize):
            counter +=1
            board[i][j] = counter
    return (board)

# Creates the horizontal grid lines 
def print_divider (boardsize):                                 
    print ('|'.join(['____' for x in range(boardsize)])) 

# Creates the spaces between the rows 
def print_blank (boardsize):
    print ('|'.join(['    ' for x in range(boardsize)]))        

# Creates the numbers for each square 
def print_labels(counter, board, boardsize):                   
    row = ' | '.join(['%2s' % board[counter][x] for x in range(boardsize)])
    row = ' ' + row
    print(row)

# Draws the complete board 
def drawBoard(board, boardsize):                                
    for i in range(boardsize):
        print_blank(boardsize)
        print_labels(i,board, boardsize)
        if (i == boardsize-1):
            print_blank(boardsize)
        else:
            print_divider(boardsize)         

# Takes a position for player 1 and updates the board
def Player_1 (board,boardsize):
    elem = 'X'
    position = inputChosenCell_1()
    board = setElem(elem, position, board)
    drawBoard(board,boardsize)
    
    # functions used to check win states 
    winhozvert = checkWin(boardsize,board)
    winbkwd = check_diag(board,'bkwd')
    winfwd = check_diag(board,'fwd')
    
    # checks if all positions are false
    if isSpace(board, boardsize) == False:
        print ("Draw!")
        exit()
    
    # Checks to see if the user has won 
    if winbkwd or winfwd or winhozvert:
        print('Congratuatlions Player 1! you win')
    else:
        Player_2(board,boardsize)

# Takes a position for player 2 and updates the board
def Player_2 (board,boardsize):
    elem = 'O'
    position = inputChosenCell_2() 
    board = setElem(elem, position, board) 
    drawBoard(board,boardsize)
    
    # functions used to check win states     
    winhozvert = checkWin(boardsize,board) 
    winbkwd = check_diag(board,'bkwd')
    winfwd = check_diag(board,'fwd')
    
    # checks if all positions are false
    if isSpace(board, boardsize) == False:
        print ("Draw!")
        exit()
    
    # Checks to see if the user has won 
    if winbkwd or winfwd or winhozvert: # Prints the player has one if won of the win states are true and if not run Player_1
        print('Congratuatlions Player 2! you win')
    else:
        Player_1(board,boardsize)
        
# Asks Player_1 for a position and return position as an integer        
def inputChosenCell_1(): 
    position = int(input("Enter a position Player 1 ")) 
    return position

# Asks Player_2 for a position and return position as an integer        
def inputChosenCell_2():
    position = int(input("Enter a position Player 2 "))
    return position 

#Checks if all the positions are taken  
def isSpace(board, boardsize):
    for i in range (boardsize):
        for j in range (boardsize):
            if board[i][j] != "X" and board[i][j] != "O":
                
                return True 
    return False

# Sets where the player counter should go on the board based on the position
def setElem (elem, position, board):
    if position == 1: 
        board [0][0] = elem
    if position == 2:
        board [0][1] = elem
    if position == 3:
        board [0][2] = elem
    if position == 4:
        board [1][0] = elem
    if position == 5:
        board [1][1] = elem
    if position == 6:
        board [1][2] = elem
    if position == 7:
        board [2][0] = elem
    if position == 8:
        board [2][1] = elem
    if position == 9:
        board [2][2] = elem 
    return board

# Checks the vertical and horizontal win states
def checkWin(boardsize,board):
    won = False
    for i in range(0,3):
        if board[i][0] == board[i][1] == board[i][2] or board[0][i] == board[1][i] == board[2][i]:
            won = True
    return won
       
# Checks the diagonal win states both forwards and backwards
def check_diag(board,direction): 
    won = False
    if direction == 'fwd':
        if board[0][0] == board[1][1] == board[2][2]:
            won = True
    elif direction == 'bkwd':
        if board[0][2] == board[1][1] == board[2][0]:
            won = True
    return (won)

# Main functions are ran to start the game
main()                                                          