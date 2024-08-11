# פונקציה לברכה
def blessing():
    print("Welcome to Tic Tac Toe!")
    print("We wish you success and enjoyment: ")
    print("Instructions: You have to choose an X or O: ")

# הדפסת לוח למשתמש  
def display_board(board):
    print("------------------")
    print(board[0],"  || ", board[1], "|| ",board [2],"||" )
    print("------------------")    
    print(board[3],"  || ", board[4],"|| ",board[5],"||")
    print("------------------")
    print(board[6],"  || ",board[7],"|| ",board[8],"||")
    print("------------------")

# בחירת X/O
def choose_symbol(symbol):
     return symbol.upper() == input("What is your choice X or O").upper()

# בדיקת בחירה של x\o
def Symbol_check():
    while True:
          symbol = input("What is your choice X or O: ").upper()
         
          if symbol == "X" or symbol == "O":
              return symbol
          else:
            print("Error\\ Choose again: X or O")
         

# קליטת בחירה מהמשתמש
def choice():
    return  int(input("We are waiting for your choice from 1 - 9: "))

# בדיקת קלט 
def check_choice():
     while True:
         try:
             
          decision = choice()

          if decision >= 1 and decision <= 9:
             return decision
          else:
             print("Error\\ Try again: the number 1 - 9")

         except ValueError:
             ס


# בדיקת לוח
def Board_check(board):
        if board[0] == board[1] == board[2] != " ":
            return board[0]
        elif board[3] == board[4] == board[5] != " ":
            return board[3]
        elif board[6] == board[7]== board[8] !=  " ":
            return board[6]
        elif board[0] == board[4] == board[8] != " ":
            return board[0]
        elif board[2] == board[4] == board[6] != " ":
            return board[2]
        elif board[2] == board[5] == board[8] != " ":
            return board[2]
        elif board[1] == board[4] == board[7] != " ":
            return board[1]
        elif board[0] == board[3] == board[6] != " ":
            return board[0]
        elif " " not in board:
            return "draw"
        else:
           return None
    
        

# הדפסת ניצחון\הפסד\תיקו
def game_over(board):
     result = Board_check(board)
     if result == "X":
         print("the winner is: X ")
     elif result == "O":
         print("the winner is: O ")
     elif result == "draw":
         print("The result is a draw")
        
     answer = input("Would you like to restart the game? (y/n): ")
    
     return answer.lower().startswith('y')        



         
# פונקציה ראשית
def Tic_Tac_Toe():
   
    blessing()

    while True:
        board = [" "] * 9

        player_symbol = Symbol_check()
        print(f"You chose: {player_symbol}")

        while True:
           display_board(board)
           position = check_choice() - 1

           if board[position] == " ":
               board[position] = player_symbol
               winner = Board_check(board)
           if winner:
                    
                    display_board(board)
                    game_over(board)
                    break  

                
           if player_symbol == "X":
                    player_symbol = "O"
           else:
                    player_symbol = "X"
        else:
            print("This position is already taken. Choose another one.")

        
        if input("Would you like to restart the game? (y/n): ").lower() != 'y':
            break 


    
          
       
if __name__ == "__main__":
     
     Tic_Tac_Toe()
      