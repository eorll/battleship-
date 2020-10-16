import os

def starting_board(rows = 5, columns = 5):
    board = []
    for column in range(rows):
        board.append(["\u001b[34;1m▉\u001b[0m"] * columns)
    
    return board


def print_board(board):
    column_number = []
    n = 0
    for i in board[0]:
        n += 1 
        column_number.append(str(n))
        column_number.append(' ')

    print("  "+"".join(column_number))
    row_number = 1
    for row in board:
        print((str(row_number)) + " " + (" ").join(row))
        row_number += 1
    
    
def get_ship_place(): 
    # Prosi o postawienie 4 statków (powietrznych) - następnie zwraca tablice z ustawieniami.
    ship_list = []
    forbidden_places = []
    board = starting_board()
    while len(ship_list) != 2:
        try:
            os.system("cls || clear")
            print_board(board)
            column_number = int(input("Enter row number: "))
            row_number = int(input("Enter column number:"))
            if [column_number - 1,row_number - 1] not in forbidden_places:
                if column_number in range(len(board[0]) + 1) and row_number in range(len(board) + 1):
                    if [column_number - 1,row_number - 1] not in ship_list:   
                        ship_list.append([column_number - 1,row_number - 1]) 
                        taken_places(forbidden_places,column_number - 1, row_number - 1)
                    else:
                        input("Place already taken!")
                else:
                    input("Enter valid coordinates!")
            else:
                input("Too close to another ship!")
            for i in ship_list:
                board[i[0]][i[1]] = "✈"
            os.system("cls || clear")
        except:
            input("Use only numbers!")
    print_board(board)
    return board


def taken_places(forbidden_places,x, y):
    # zapewnia 1 pole odstępu pomiędzy statkami

    forbidden_places.append([x-1,y-1])
    forbidden_places.append([x,y-1])
    forbidden_places.append([x+1,y-1])
    forbidden_places.append([x-1,y])
    forbidden_places.append([x+1,y])
    forbidden_places.append([x-1,y+1])
    forbidden_places.append([x,y+1])
    forbidden_places.append([x+1,y+1])

    return forbidden_places

    

def get_player_move(player_moves): 
    # Bierze tablice ruchów gracza i sprawdza czy ruch jest możliwy do wykonania, jeśli tak zwraca koordynaty - najlepiej do funkcji is_hit i is_sunk!
    while True:
        print_board(player_moves)
        try:
            column_number = int(input("Column number: "))
            row_number = int(input("Row number: "))

            if player_moves[row_number - 1][column_number - 1] == '\u001b[34;1m▉\u001b[0m': 
                return [row_number -1, column_number -1]
            else: 
                input("Pleas enter valid move!")
            os.system("cls || clear")
        except: 
            input("Enter only numbers!")
  
    
def is_hit(player_X_ship, player_Y_moves, coordinates): 
    # powinna brać tablice player_X_ships i koordynaty z get_player_move i zwracać hit lub miss na tablicy  player_Y_moves ≋ ☠
    if player_X_ship[coordinates[0]][coordinates[1]] == "✈":
        player_Y_moves[coordinates[0]][coordinates[1]] = '\u001b[31m☠\u001b[0m'
        os.system("cls || clear")
        print_board(player_Y_moves)
        print('     HIT')
    else:
        player_Y_moves[coordinates[0]][coordinates[1]] = '≋'
        os.system("cls || clear")
        print_board(player_Y_moves)
        print("     MISS")
    return player_Y_moves

def is_sunk():
    # na razie nie potrzebna
    pass

def mark():
    # is_hit bierze to na siebie
    pass

def has_won(player_X_ships, player_Y_moves):
    move_test = []
    ship_test = []

    for i in player_Y_moves:
        for j in i:
            if j == '\u001b[31m☠\u001b[0m':
                move_test.append('\u001b[31m☠\u001b[0m')

    for i in player_X_ships:
        for j in i:
            if j == '✈':
                ship_test.append('\u001b[31m☠\u001b[0m')
    
    if move_test == ship_test:
        return True
    else:
        return False


def print_result():
    pass 

def menu():
    pass 

def battleship_game():

# board; players_1_ships; player_2_ships; player_1_moves; player_2_moves

    player_1_moves = starting_board()
    player_2_moves = starting_board()
    input("Player 1 - Press Enter ")
    player_1_ships = get_ship_place()
    input("Player 2 - Press Enter  ")
    player_2_ships = get_ship_place()

    while True:
        
        input("Player 1 - Press Enter ")
        os.system("cls || clear")
        is_hit(player_2_ships, player_1_moves, get_player_move(player_1_moves))
        if has_won(player_2_ships,player_1_moves) == True:
            print('Player 1 - WON')
            break
        
        input("Player 2 - Press Enter ")
        os.system("cls || clear")
        is_hit(player_1_ships, player_2_moves, get_player_move(player_2_moves))
        if has_won(player_1_ships,player_2_moves) == True:
            print('Player 2 - WON')
            break

        
battleship_game()     



