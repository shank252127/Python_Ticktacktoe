#Required Imports;
import os;
import random;

#Function to display board for the game;
def display_board(board):
    #Clear Screen;
    os.system('cls')

    #Setting up the game board;
    print('\n')
    print('    |    |')
    print('  '+ board[7]+' |  '+board[8]+ ' | '+board[9])
    print('    |    |')
    print('-------------')
     
    print('    |    |')
    print('  '+ board[4]+' |  '+board[5]+ ' | '+board[6])
    print('    |    |')
    print('-------------')
    
    print('    |    |')
    print('  '+ board[1]+' |  '+board[2]+ ' | '+board[3])
    print('    |    |')
    

#Assigning User a Player name i.e. Player 1 or Player 2;
def player_assignment():  
    identifier = ''
    while identifier !='X'  and identifier !='O' :
        identifier = input('Player1 : Choose X or O: ').upper()
    if identifier=='X' :
        return ('X','O')
    else:
        return ('O','X')

#Fill a position entered by player with X/O; 
def place_marker(board,identifier,position):
    board[position]=identifier
    
#It check for the winner;
def winner_check(board,mark):
    if ((board[9]==board[8]==board[7]==mark) or #row 1
            (board[6]==board[5]==board[4]==mark) or #row 2
            (board[3]==board[2]==board[1]==mark) or #row 3
            (board[9]==board[6]==board[3]==mark) or #column 1
            (board[8]==board[5]==board[2]==mark) or #column 2
            (board[7]==board[4]==board[1]==mark) or #column 3
            (board[3]==board[5]==board[7]==mark) or #diagonal 1
            (board[1]==board[5]==board[9]==mark)):  #diagonal 2
        return True
    return False

#Choosing which player to go first;
def choose_First():
    who_First=random.randint(0,1)
    if who_First==1:
        return 'Player 1'
    else:
        return 'Player 2'
    
#Check whether the position is available;
def availability_check(board,position):
    if board[position] !=' ' :
        print("This position is already occupied !!!")  
    return board[position]==' ';
  
#Checks whether all position in the game board is full or not;  
def full_board_check(board):
    for i in range(1,10):
        if availability_check(board, i):
            return False;        
    return True

#Take as input the position in the board the user want to fill;
def player_choice(board):
    position=0;    
    position_array= [1,2,3,4,5,6,7,8,9] 
    count=0
    while position not in position_array or not availability_check(board, position):
        if(count==0):
            position = int(input('Choose a position: (1-9)'))   
        else: 
            if(position>9 or position<0):                           
                print("Enter the position within the range of board !!!")     
            position = int(input('Choose a position: (1-9)'))   
        count+=1
    return position
        
#Ask User for replay/reset the game;  
def replay():
    user_choice = input('Play Again ? Y or N').upper()   
    return user_choice=='Y'

#Game Starts;
print("Welcome to TickTackToe")
#This is the loop which call the above function in the game logically;
#Will run until and unless it breaks ;
while True:   
    #Game will run till the "game_on" remains False;
    game_on=False
    count=0
    the_board= [' ']*10
    player1_Marker,player2_Marker = player_assignment()
    
    turn =choose_First()
    print(turn + ' will go first')
    
    play_game=input("Ready to play? Y or N").upper()
    
    if play_game == 'Y':
        game_on=True
    else: 
        game_on=False
    
   
    while game_on:
        count+=1
        #Player 1 Turn;
        if turn =='Player 1':        
            display_board(the_board)           
            position = player_choice(the_board)       
            
            place_marker(the_board,player1_Marker , position)
            
            if winner_check(the_board,player1_Marker):      
                display_board(the_board)
                print("Player 1 has won !!!")
                game_on=False
            else:
                if full_board_check(the_board):              
                    display_board(the_board)
                    print(" Tie Game !!!")
                    game_on=False
                else:                
                    turn ='Player 2'
                
        else:
            #Player 2 Turn;
            display_board(the_board)            
            position = player_choice(the_board)
            
            place_marker(the_board,player2_Marker , position)            
            if winner_check(the_board,player2_Marker):
                display_board(the_board)
                print("Player 2 has won !!!")
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print(" Tie Game !!!")
                    game_on=False
                else:
                    turn ='Player 1'
                
            
    
    #This will break the above while loop;
    #Will End the Game;
    if count==0:
        print("Game End !!!")
        print("Run the program to play again ...")
        break;
    else:
        if not replay():
            print("Game End !!!")
            print("Run the program to play again ...")
            break;
    

    
    
    
    


     
    
    
