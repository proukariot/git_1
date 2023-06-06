from IPython.display import clear_output
def display_board(board):
    clear_output()  # działa tylko w jupyter
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)
   |   |
 X | O | X
   |   |
-----------
   |   |
 O | X | O
   |   |
-----------
   |   |
 X | O | X
   |   |
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Gracz 1: chcesz być X czy O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
def place_marker(board, marker, position):
    board[position] = marker
def win_check(board,mark): #sprawdzamy czy ktoś wygrał
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # po górnej linii
    (board[4] == mark and board[5] == mark and board[6] == mark) or # przez środek
    (board[1] == mark and board[2] == mark and board[3] == mark) or # przez dół
    (board[7] == mark and board[4] == mark and board[1] == mark) or # lewo - dół
    (board[8] == mark and board[5] == mark and board[2] == mark) or # środek - dół
    (board[9] == mark and board[6] == mark and board[3] == mark) or # prawo - dół
    (board[7] == mark and board[5] == mark and board[3] == mark) or # przekątna
    (board[9] == mark and board[5] == mark and board[1] == mark)) # przekątna
import random #randomowo wybieramy pierwszego

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Gracz 2'
    else:
        return 'Gracz 1'
def space_check(board, position): # sprawdzamy czy pola są puste
    
    return board[position] == ' '
def full_board_check(board): # sprawdzamy czy wszytkie pola wypełnione
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
def player_choice(board): #gracz wybiera pole, jeśli wolne 
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Wybierz następne pole: (1-9) '))
        
    return position
def replay():
    
    return input('Chcesz zagrać jeszcze raz? Wpisz Tak lub Nie: ').lower().startswith('t')
print('Zapraszam do gry w kółko - krzyżyk!')

while True:
    # zerujemy pola
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' wybiera pierwszy.')
    
    play_game = input('Gotowy do gry? Wpisz Tak lub Nie.')
    
    if play_game.lower()[0] == 't':
        game_on = True
    else:
        game_on = False
        
        
        
    while game_on:
        if turn == 'Gracz 1':
            # Ruch 1 gracza.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Gratulacje! Wygrałeś grę!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Nikt nie przegrał!')
                    break
                else:
                    turn = 'Gracz 2'
        else:
            # Ruch 2 gracza.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Gracz 2 wygrał!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Nikt nie przegrał!')
                    break
                else:
                    turn = 'Gracz 1'
    if not replay():
        break
