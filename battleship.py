def starting_board(rows = 5, columns = 5):
    board = []
    for column in range(rows):
        board.append(["▉"] * columns)
    
    return board

def print_board(board):
    for row in board:
        print((" ").join(row))

def get_ship_place() #Pobieranie od uzytkownika miesca statków, zapisywanie i zwaracanie współrzędnych. Ustalenie rodzaju i ilosci statkow 
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

# board; players1_ships; player2_ships; player_1_moves; player_2_moves; 

Player1_ships = get_ship_place()
Player2_ships = get_ship_place()
Player1_moves = starting_board()
Player2_moves = starting_board()

n = 0

while has_won() == False:
    print_board(Player1_moves)
    print_board(Player2_moves)
    if n = 0: 
        Player1_moves = get_player_move(Player1_moves)



        n +=1 
    if n = 1: 
        Player2_moves = get_player_move(Player2_moves)  


        n -=1 
    





board = starting_board() 

print_board(board)


