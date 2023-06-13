import random
default_board = ['.' for x in range(10)]
board = ['.' for x in range(10)]
def insertMyletter(board, pos):
    board[pos]= "x"
   
def insertCompletter(board, comp_pos):
    board[comp_pos] = "o"    

def printBoard(board):
    print(board[1], board[2], board[3]) 
    print(board[4], board[5], board[6])
    print(board[7], board[8], board[9])


def isWinner(board, le):
    if board[1]== board[5] == board[9]== le or board[7] == board[5] == board[3]== le or board [1]== board[4]==board[7]==le or board[2]==board[5]==board[8]==le or board[3]==board[6]==board[9]==le or board[1]==board[2]==board[3]==le or board[4]==board[5]==board[6]==le or board[7]==board[8]==board[9]==le :
        printBoard(board)

        if le == 'x':
            print('You won!')
            board = default_board
            ask_play_again(play_again)

        if le == 'o':
            print('Computer won!')
            board = default_board
            ask_play_again(play_again)  

play_again = ""
def ask_play_again(play_again):
    while True:
        play_again = input("Play again? (y/n) ").lower()
        if play_again == "y":
            
            board = ['.' for x in range(10)]
            player_move(board, pos= pos)
            
        elif play_again == "n":
            quit()
        else:
            print ("Invalid answer")
            continue    
          
                       

def isBoardFull(board):
    if board[1]!= "." and board[2]!= "." and board[3]!= "." and board[4]!= "." and board[5]!= "." and board[6]!= "." and board[7]!= "." and board[8]!= "." and board[9]!= ".":
        
        printBoard(board)
        print("Tie Game!")
        board = default_board
        ask_play_again(play_again)
        

pos = 0
def player_move(board, pos):
    

    while True:

        printBoard(board)
        isBoardFull(board)
        pos = input ("Enter position (1-9): ")
        if not pos.isdigit():
            print("Please type a number")
            continue
       
        pos = int(pos)

        if pos>9 or pos<1:
            print("Invalid number")
            continue 
        if board[pos] != ".":
            print("Spot already taken")
            continue
        
        insertMyletter(board, pos)
        isWinner(board, "x")
        isBoardFull(board)
        comp_pos= 1
        comp_move(board, comp_pos)

def comp_move(board, comp_pos):
    pos= 1


    #FILL ROW 1
    if board[1]==board[2]== "o" and board[3]=="." :
        comp_pos = 3
    elif board[2]==board[3]== "o" and board[1]=="." :
        comp_pos = 1
    elif board[1]==board[3]== "o" and board[2]=="." :
        comp_pos = 2   
    #FILL ROW 2
    elif board[4]==board[5]== "o" and board[6]=="." :
        comp_pos = 6
    elif board[5]==board[6]== "o" and board[4]=="." :
        comp_pos = 4
    elif board[4]==board[6]== "o" and board[5]=="." :
        comp_pos = 5 
    #FILL ROW 3
    elif board[7]==board[8]== "o" and board[9]=="." :
        comp_pos = 9
    elif board[8]==board[9]== "o" and board[7]=="." :
        comp_pos = 7
    elif board[7]==board[9]== "o" and board[8]=="." :
        comp_pos = 8


    #FILL COLUMN 1
    elif board[1]==board[4]== "o" and board[7]=="." :
        comp_pos = 7
    elif board[4]==board[7]== "o" and board[1]=="." :
        comp_pos = 1
    elif board[1]==board[7]== "o" and board[4]=="." :
        comp_pos = 4   
    #FILL COLUMN 2
    elif board[2]==board[5]== "o" and board[8]=="." :
        comp_pos = 8
    elif board[5]==board[8]== "o" and board[2]=="." :
        comp_pos = 2
    elif board[2]==board[8]== "o" and board[5]=="." :
        comp_pos = 5 
    #FILL COLUMN 3
    elif board[3]==board[6]== "o" and board[9]=="." :
        comp_pos = 9
    elif board[6]==board[9]== "o" and board[3]=="." :
        comp_pos = 3
    elif board[3]==board[9]== "o" and board[6]=="." :
        comp_pos = 6    


    #FILL DIAGONAL 1
    elif board[1]==board[5]== "o" and board[9]=="." :
        comp_pos = 9
    elif board[5]==board[9]== "o" and board[1]=="." :
        comp_pos = 1
    elif board[1]==board[9]== "o" and board[5]=="." :
        comp_pos = 5

    #FILL DIAGONAL 2
    elif board[7]==board[5]== "o" and board[3]=="." :
        comp_pos = 3
    elif board[5]==board[3]== "o" and board[7]=="." :
        comp_pos = 7
    elif board[7]==board[3]== "o" and board[5]=="." :
        comp_pos = 5 








    

    #FILL ROW 1
    elif board[1]==board[2]== "x" and board[3]=="." :
        comp_pos = 3
    elif board[2]==board[3]== "x" and board[1]=="." :
        comp_pos = 1
    elif board[1]==board[3]== "x" and board[2]=="." :
        comp_pos = 2   
    #FILL ROW 2
    elif board[4]==board[5]== "x" and board[6]=="." :
        comp_pos = 6
    elif board[5]==board[6]== "x" and board[4]=="." :
        comp_pos = 4
    elif board[4]==board[6]== "x" and board[5]=="." :
        comp_pos = 5 
    #FILL ROW 3
    elif board[7]==board[8]== "x" and board[9]=="." :
        comp_pos = 9
    elif board[8]==board[9]== "x" and board[7]=="." :
        comp_pos = 7
    elif board[7]==board[9]== "x" and board[8]=="." :
        comp_pos = 8


    #FILL COLUMN 1
    elif board[1]==board[4]== "x" and board[7]=="." :
        comp_pos = 7
    elif board[4]==board[7]== "x" and board[1]=="." :
        comp_pos = 1
    elif board[1]==board[7]== "x" and board[4]=="." :
        comp_pos = 4   
    #FILL COLUMN 2
    elif board[2]==board[5]== "x" and board[8]=="." :
        comp_pos = 8
    elif board[5]==board[8]== "x" and board[2]=="." :
        comp_pos = 2
    elif board[2]==board[8]== "x" and board[5]=="." :
        comp_pos = 5 
    #FILL COLUMN 3
    elif board[3]==board[6]== "x" and board[9]=="." :
        comp_pos = 9
    elif board[6]==board[9]== "x" and board[3]=="." :
        comp_pos = 3
    elif board[3]==board[9]== "x" and board[6]=="." :
        comp_pos = 6    


    #FILL DIAGONAL 1
    elif board[1]==board[5]== "x" and board[9]=="." :
        comp_pos = 9
    elif board[5]==board[9]== "x" and board[1]=="." :
        comp_pos = 1
    elif board[1]==board[9]== "x" and board[5]=="." :
        comp_pos = 5

    #FILL DIAGONAL 2
    elif board[7]==board[5]== "x" and board[3]=="." :
        comp_pos = 3
    elif board[5]==board[3]== "x" and board[7]=="." :
        comp_pos = 7
    elif board[7]==board[3]== "x" and board[5]=="." :
        comp_pos = 5 



    else:
    
    
        #BLOCK MOVEMENT
        while True:
            
            if board[1]!= "." and "." in [board[2],board[4],board[5]]:
                comp_pos = random.choice([2,4,5])
                if board[comp_pos] != ".":
                    continue
                break

            if board[2]!= "." and "." in [board[1],board[3],board[5]]:
                comp_pos = random.choice([1,3,5])
                if board[comp_pos] != ".":
                    continue
                break

            if board[3]!= "." and "." in [board[2],board[5],board[6]]:
                comp_pos = random.choice([2,5,6])
                if board[comp_pos] != ".":
                    continue
                break
            
            if board[4]!= "." and "." in [board[1],board[5],board[7]]:
                comp_pos = random.choice([1,5,7])
                if board[comp_pos] != ".":
                    continue
                break

            if board[5]!= "." and "." in board:
                comp_pos = random.choice([1,2,3,4,5,6,7,8,9])
                if board[comp_pos] != ".":
                    continue
                break

            if board[6]!= "." and "." in [board[3],board[5],board[9]]:
                comp_pos = random.choice([3,5,9])
                if board[comp_pos] != ".":
                    continue
                break
            
            if board[7]!= "." and "." in [board[4],board[5],board[8]]:
                comp_pos = random.choice([4,5,8])
                if board[comp_pos] != ".":
                    continue
                break

            if board[8]!= "." and "." in [board[5],board[7],board[9]]:
                comp_pos = random.choice([5,7,9])
                if board[comp_pos] != ".":
                    continue
                break

            if board[9]!= "." and "." in [board[5],board[6],board[8]]:
                comp_pos = random.choice([5,6,8])
                if board[comp_pos] != ".":
                    continue
                break


        


        

    insertCompletter(board, comp_pos)
        

    print ("Computer chose position", comp_pos)
    isWinner(board, "o")
    isBoardFull(board)
    player_move(board, pos)    


player_move(default_board, 1)