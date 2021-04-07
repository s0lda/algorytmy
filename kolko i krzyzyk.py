def display_board(board):
    blankboard = '''
_________________________
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
|-------|-------|-------|
|       |       |       |
|   4   |   5   |   6   |
|       |       |       |
|-------|-------|-------|
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
|_______|_______|_______|
'''
    for i in range(1,10):
        if (board[i] == '0' or board[i] == 'X'):
            blankboard = blankboard.replace(str(i), board[i])
        else:
            blankboard = blankboard.replace(str(i), ' ')
    print(blankboard)

def player_input():
    player1 = input("Wybierasz 'O' czy 'X' ?")
    if player1.upper() == 'X':
        player2 = 'O'
        print('Wybrałeś ' + player1 + 'przeciwnik będzie miał ' + player2)
        return player1.upper(), player2
    elif player1.upper() == 'O':
        player2 = 'X'
        print('Wybrałeś ' + player1 + 'przeciwnik będzie miał ' + player2)
        return player1.upper(), player2
    else:
        player1 = input("Wybierasz 'O' czy 'X' ?")

def place_marker(board, marker, position):
    board[position] = marker
    return board

def space_check(board, position):
    return board[position] == '#'

def player_choice(board):
    choice = input('Wybierz pole pomiędzy 1 a 9: ')
    while not space_check(board, int(choice)):
        choice = input('To miejsce jest juz zajęte, wybierz inne.. ')
        return choice

def full_board_check(board):
    return len([x for x in board if x == '#']) == 1

def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[3] == board[6] == board[9] == mark:
        return True
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True
    return False

def replay():
    play_again = input('Chesz zagrać jeszcze raz? ')
    if play_again.lower() == 't' or 'y' or 'tak' or 'yes':
        return True
    if play_again.lower() == 'n' or 'nie' or 'no':
        return False

if __name__ == '__main__':
    print('Witamy w Kółko i Krzyżyk')
    i = 1
    players = player_input()
    board = ['#'] * 10
    while True:
        game_on = full_board_check(board)
        while not game_on:
            position = player_choice(board)
            if i % 2 == 0:
                marker = players[1]
            else:
                marker = players[0]
            place_marker(board, marker, int(position))
            display_board(board)
            i += 1
            if win_check(board, marker):
                print('Wygrałeś!')
                break
            game_on = full_board_check(board)
        if not replay():
            break
        else:
            i = 1
            player = player_input()
            board = ['#'] * 10