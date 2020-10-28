grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,0,9]]
        
def check_possible(i, j, k):
    if (k in grid[i]):
        return False
    for m in range(9):
        if (grid[m][j] == k):
            return False
    i0 = (i // 3) * 3
    j0 = (j // 3) * 3
    for n in range(3):
        for o in range(3):
            if (grid[i0 + n][j0 + o] == k):
                return False
    return True

def print_sudoku():
    for i in range(9):
        if (i == 3 or i == 6):
            print("--------------------------------\n")
        for j in range(9):
            if (j == 3 or j == 6):
                print('|  ', end="")
            print(grid[i][j], end="")
            print('  ', end="")
            if (j == 8):
                print('\n')


def solve():
    for i in range(9):
        for j in range(9):
            if (grid[i][j] == 0):
                    for k in range (1,10):
                        if check_possible(i, j, k):
                            grid[i][j] = k
                            solve()
                            grid[i][j] = 0
                    return
    print_sudoku()
    input("D'autres ?")
    
solve()
