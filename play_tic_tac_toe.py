from random import randrange 
    
def display_board(board):
    line = '+-------' * 3 + '+'
    line2 = '|       ' * 3 + '|'
    line3 = '|   ' + str(board[0][0]) + '   ' + '|   ' + str(board[0][1]) + '   ' + '|   ' + str(board[0][2]) + '   ' + '|'
    line4 = '|   ' + str(board[1][0]) + '   ' + '|   ' + str(board[1][1]) + '   ' + '|   ' + str(board[1][2]) + '   ' + '|'
    line5 = '|   ' + str(board[2][0]) + '   ' + '|   ' + str(board[2][1]) + '   ' + '|   ' + str(board[2][2]) + '   ' + '|'
    print(line)
    print(line2)
    print(line3)
    print(line2)
    print(line)
    print(line2)
    print(line4)
    print(line2)
    print(line)
    print(line2)
    print(line5)
    print(line2)
    print(line)

def enter_move(board):
    try:
        move = int(input('Enter your move: '))
        x = move // 3 + (move % 3 > 0) - 1
        if move % 3 == 0:
            y = 2
        elif move in (2, 5, 8):
            y = 1
        else:
            y = 0
        if (x, y) in make_list_of_free_fields(board):
            board[x][y] = 'O'
        else:
            print('That move is taken. Choose a different move.')
    except:
        print('Move must be an int greater than 0 and less than 10.')

def make_list_of_free_fields(board):
    free_spaces = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            if isinstance(board[x][y], int):
                free_spaces.append((x, y))
                
    return free_spaces

def victory_for(board, sign):
    win_list = [['O', 'O', 'O'], ['X', 'X', 'X']]
    
    for x in range(3):
        if board[x] in win_list:
            return True
            
    for y in range(3):
        vertical_list = []
        for x in range(3):
            vertical_list.append(board[x][y])
        if vertical_list in win_list:
            return True
            
    if [board[0][0], board[1][1], board[2][2]] in win_list or [board[0][2], board[1][1], board[2][0]] in win_list:
        return True
        
    return False

def draw_move(board):
    move_completed = False
    while move_completed == False:
        move = randrange(10)
        x = move // 3 + (move % 3 > 0) - 1
        if move % 3 == 0:
            y = 2
        elif move in (2, 5, 8):
            y = 1
        else:
            y = 0
        if (x, y) in make_list_of_free_fields(board):
            board[x][y] = 'X'
            move_completed = True

def main():
    board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
    end_game = False
    while end_game == False:       
        display_board(board)
        enter_move(board)
        if victory_for(board, 'O') == True:
            end_game = True
            display_board(board)
            return print('You won!')
        draw_move(board)
        if victory_for(board, 'X') == True:
            end_game = True
            display_board(board)
            return print('Computer won!')
        if len(make_list_of_free_fields(board)) == 0:
            end_game = True
            return print('Tie game!')

if __name__ == '__main__':
    main()