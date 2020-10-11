def starting_board(rows = 5, columns = 5):
    board = []
    for column in range(rows):
        board.append(["▉"] * columns)
    
    return board

def print_board(board):
    for row in board:
        print((" ").join(row))
def get_ship_place(): 
     # Prosi o postawienie 4 statków (powietrznych) - następnie zwraca tablice z ustawieniami.
     ship_list = []
     board = starting_board()
     while len(ship_list) != 3:
         try:
             print_board(board)
             column_number = int(input("Enter row number: "))
             row_number = int(input("Enter column number:"))
             if column_number in range(len(board[0]) + 1) and row_number in range(len(board) + 1):
                 if [column_number - 1,row_number - 1] not in ship_list:   
                     ship_list.append([column_number - 1,row_number - 1]) 
                 else:
                     print("Place already taken!")
             else:
                 print("Enter valid coordinates!")
             for i in ship_list:
                 board[i[0]][i[1]] = "✈"
             input("Press enter to continue.")
             os.system("cls || clear")
         except:
             print("Only numbers!")
     return board


 #def get_ship_place(): #Pobieranie od uzytkownika miesca statków, zapisywanie i zwaracanie współrzędnych 
    # pass

 def get_player_move(total_moves): 
     

    if total_moves % 2 == 0:
        total_moves += 1
        return player_1_moves

    return player_2_moves

# Allows new game to start
def play_again():

    play_one-more_time = ["yes", "y"] 
    play_not = ["no", "n"]

    while True
        answer = input("Play again? [Y(es) / N(o)]: ").lower().strip()
        if answer in play_one_more_time:
            battleship_game()
            main()
            
            break

        elif answer in play_not:   
            print("Thanks for playing!")
            exit()

     pass

 def is_hit(): 

     is_hit = 0

    for player_moves in range(4):
        guess_row = input("Guess Row: (allowed values: 0-4) ")
        guess_col = input("Guess Col: (allowed values: 0-4) ")

        if (guess_row == column_number in range(len(board[0]) + 1)  and guess_col == ship_list) or (guess_row == row_number in range(len(board) + 1 and guess_row == ship_list):
            is_hit = is_hit + 1
            board[guess_row][guess_col] = "*"
            print ("Congratulations! ")
            if is_hit == 1:
                   print("You sunk first battleship!") 
            elif is_hit == 2:
                   print("You sunk second battleship! You win!")
                   print_board(board)
                   break
        else:
            if (guess_row < 0 or guess_row > 4)  or (guess_col < 0 or guess_col > 4):
                   print ("Oops, that's not even in the ocean.")
            elif(board[guess_row][guess_col] == "X"):
                   print ("You guessed that one already.")
            else:
                 print ("You missed my battleship!")
                 board[guess_row][guess_col] = "X"
            print (player_moves + 1, "enter")
     print_board(board)


 def get_player_move(player_moves): 
     # Bierze tablice ruchów gracza i sprawdza czy ruch jest możliwy do wykonania, jeśli tak zwraca koordynaty - najlepiej do funkcji is_hit i is_sunk!
     while True:
         print_board(player_moves)
         try:
             column_number = int(input("Column number: "))
             row_number = int(input("Row number: "))

             if player_moves[row_number][column_number] == '▉': 
                 return row_number, column_number
             else: 
                 input("Pleas enter valid move!")
             input("Press enter to continue.")
             os.system("cls || clear")
         except: 
             input("Enter only numbers!")


 #def is_hit(player_X_ship, player_Y_moves, coordinates): 
     # powinna brać tablice player_X_ships i koordynaty z get_player_move i zwracać hit lub miss na tablicy  player_Y_moves
     #pass

 def is_sunk():
     # na razie nie potrzebna
     pass

 def mark():
     # is_hit bierze to na siebie
     pass

 def has_won():
     pass
 def has_won(players_1_ships, player_2_ships, player_1_moves, player_2_moves):
     # porównuje tablice player_X_ships z tablicą player_Y_moves - jeśli wszystkie cele są zastrzelone zwraca True 
     return False

 def print_result():
     pass 
 def battleship_game():

     player_1_moves = starting_board()
     player_2_moves = starting_board()
     players_1_ships = get_ship_place()
     input("Player 1 - Press Enter ")
     player_1_ships = get_ship_place()
     input("Player 2 - Press Enter  ")
     player_2_ships = get_ship_place()

     while has_won() == False:

         break
     while has_won(player_1_ships, player_2_ships, player_1_moves, player_2_moves) == False:
         input("Player 1 - Press Enter ")
         is_hit(player_2_ships, player_1_moves, get_player_move(player_1_moves))
         input("Player 2 - Press Enter ")
         is_hit(player_1_ships, player_2_moves, get_player_move(player_2_moves))
 battleship_game() 

 def(main):
       for moves in range(6):

        if player_moves(moves) == player_1_moves:
            print("Player One")
                 

        elif player_moves(moves) == player_2_moves:
            print("Player Two")
            
            
        if moves == 10:
            print("This game is a tie.")
            print_board(board)
            play_again()


if __name__ == "__main__":
    main() 



def get_ship_place() #Pobieranie od uzytkownika miesca statków, zapisywanie i zwaracanie współrzędnych 
    pass

def get_player_move() #
    pass

def is_hit() 
    pass

def is_sunk()
    pass

def mark()
    pass

def has_won()
    pass

def print_result()
    pass 

def menu()
    pass 

def battleship_game()

# board; players1_ships; player2_ships; player_1_moves; player_2_moves

while has_won() == False





board = starting_board() 

print_board(board)


