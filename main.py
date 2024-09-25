#creating board 
board = ["0", "1", "2",
         "3", "4", "5",
         "6", "7", "8"]
winner = False
current_player = 'X'
turn =0

#taking player input and printing board 
print("Welcome to Tic Tak Toe")
one = input("Enter user 1: ")
two = input("Enter user 2: ")
while not winner and turn < 9:
        print(board [0] + " | " + board[1] + " | " + board[2])
        print("----------")
        print(board [3] + " | " + board[4] + " | " + board[5])
        print("----------")
        print(board [6] + " | " + board[7] + " | " + board[8])
        #asking player to play their move 
        if current_player =='X':
              print (one + "'s chance")
        else:
              print (two +"'s chance")
        try:
                move = int(input("choose a position from 0-8 : "))

        except ValueError:
                print("Invalid input")
                continue
        #invalid move 
        if move < 0 or move > 8 or board[move]==' ':
            print ("Invalid move, try again")
            continue 
        
        board[move] = current_player
        turn +=1

        #check for win 
        if (board[0] == board[1] == board[2] == current_player or 
            board[3] == board[4] == board[5] == current_player or 
            board[6] == board[7] == board[8] == current_player or 
            board[0] == board[3] == board[6] == current_player or 
            board[1] == board[4] == board[7] == current_player or 
            board[2] == board[5] == board[8] == current_player or 
            board[0] == board[4] == board[8] == current_player or 
            board[2] == board[4] == board[6] == current_player ):
                winner = True
                break
        
        #Changing player 
        if current_player == 'X':
            current_player ='O'
        else:
            current_player = 'X'
        #Final board display
        print(f"\n{board [0]} | {board[1]} | {board[2]}")
        print("----------")
        print(f"\n{board [3]} | {board[4]} | {board[5]}")
        print("----------")
        print(f"\n{board [6]} | {board[7]} | {board[8]}")
        print("\n") 
    
    #Game result
if winner:
    print(f"\nPlayer {current_player    } wins!")
else:
    print("\nIt's a tie!")
