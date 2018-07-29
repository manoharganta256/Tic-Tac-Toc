from string import ascii_lowercase,digits
from random import randint
def set_grid():
    grid = [[' ' for i in range(3)] for i in range(3)]
    show_grid(grid)
    return grid
def show_grid(grid):
    grid_size = len(grid)
    toplabel = '    '
    for i in ascii_lowercase[:grid_size]:
        toplabel+=i+'   '
    print(toplabel)
    for i in range(grid_size):
        s = str(i)+' | '
        for j in range(grid_size):
            s+=str(grid[i][j])+' | '
        horizontal = '----'*grid_size
        print('   '+horizontal)
        print(s)
    print('   '+horizontal)
def who_plays_first():
    return randint(0,1)
def make_move(grid):
    free_cells = []
    for i in range(0,3):
        for j in range(0,3):
            if grid[i][j] == ' ':
                free_cells.append((i,j))
    # check if computer is winning 
    for x,y in free_cells:
        grid[x][y] = 'O'
        if is_winning(grid,'O'):
            return
        else:
            grid[x][y] = ' '
    # check if human is winning
    for x,y in free_cells:
        grid[x][y] = 'X'
        if is_winning(grid,'X'):
            grid[x][y] = 'O'
            return
        else:
            grid[x][y] = ' '
    # take corners
    corners = list(set([(0,0),(0,2),(2,0),(2,2)]).intersection(free_cells))
    if len(corners) > 0:
        x,y = corners[randint(0,len(corners)-1)]
        grid[x][y] = 'O'
        return
    # take center
    if grid[1][1] == ' ':
        grid[1][1] = 'O'
        return
    # take edges
    sides = list(set([(0,1),(1,0),(1,2),(2,1)]).intersection(free_cells))
    if len(sides) > 0:
        x,y = sides[randint(0,len(sides)-1)]
        grid[x][y] = 'O'
        return
def is_winning(grid,letter):
    return ((grid[0][0] == grid[0][1] == grid[0][2] == letter) or 
    (grid[1][0] == grid[1][1] == grid[1][2] == letter) or
    (grid[2][0] == grid[2][1] == grid[2][2] == letter) or
    (grid[0][0] == grid[1][0] == grid[2][0] == letter) or
    (grid[0][1] == grid[1][1] == grid[2][1] == letter) or
    (grid[0][2] == grid[1][2] == grid[2][2] == letter) or
    (grid[0][0] == grid[1][1] == grid[2][2] == letter) or
    (grid[0][2] == grid[1][1] == grid[2][0] == letter))   
def is_board_full(grid):
    free_cells = []
    for i in range(0,3):
        for j in range(0,3):
            if grid[i][j] == ' ':
                free_cells.append((i,j))
    return True if len(free_cells) == 0 else False
def play_game():
    grid = set_grid()
    grid_size = len(grid)
    print('Type the column followed by the row (eg. b1).')
    if who_plays_first():
        print('You play first with X !')
        human = True
    else:
        print('Computer plays first with O!')
        human = False
    while True:
        if human:
            print('Your turn Enter cell : ',end='')
            cell = input()
            if cell[0] in ascii_lowercase[:grid_size] and cell[1] in digits[:grid_size] and len(cell) == 2:
                row = int(cell[1])
                col = ord(cell[0]) - ord('a')
                if grid[row][col] != ' ':
                    print('Cell already full')
                    continue
                grid[row][col] = 'X'
                show_grid(grid)
                if is_winning(grid,'X'):
                    print('You Won')
                    break
                if is_board_full(grid):
                    print('Tie')
                    break
                print('Computers turn')
                make_move(grid)
                show_grid(grid)
                if is_winning(grid,'O'):
                    print('Computer Won')
                    break
            else:
                print('Invalid Cell')
        else:
            print('Computers turn')
            make_move(grid)
            show_grid(grid)
            if is_winning(grid,'O'):
                print('Computer Won')
                break
            if is_board_full(grid):
                print('Tie')
                break
            while True:
                print('Your turn Enter cell : ',end='')
                cell = input()
                if cell[0] in ascii_lowercase[:grid_size] and cell[1] in digits[:grid_size] and len(cell) == 2:
                    row = int(cell[1])
                    col = ord(cell[0]) - ord('a')
                    if grid[row][col] != ' ':
                        print('Cell already full')
                        continue
                    grid[row][col] = 'X'
                    show_grid(grid)
                    break
                else:
                    print('Invalid Cell')
            if is_winning(grid,'X'):
                print('You Won')
                break
play_game()
