# This is a sample Python script.

# a validation function that will check for a valid try, i.e., acceptable for that cell.
# /we are asking  in this grid at this position is this  number a valid move or not. If not  we will not do it
def is_valid_move(grid, row, col, number):
    #we have to check is there is a same number in the same row, or same column or same block.

    #CHECKING FOR ROWS
    for x in range(9):
        # if the grid in that specific row for each x in that row if we have the same numner than return false
        if grid[row][x] == number:
            return False
        
    #CHECKING FOR COLUMNS   
    for x in range(9):
        # if the grid in that specific column for each x in that column if we have the same numner than return false
        if grid[x][col] == number:
            return False
        
    # CHECKING FOR BLOCK
    #first we need to find the corner row
    corner_row = row - row % 3
    corner_col = col - col % 3

    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False
    
    return True


# Backtracking function is called solve

def solve(grid, row, col):
    if col == 9: # this is overflowing bcz the last col val will be 8
        if row == 8:  # this is last row
            # if the above both are true it means we have reach an end of the sudoku
            # THAT IS THE SUDOKU IS SOLVED
            return True
        row += 1
        col = 0

    # this means that particular position is already solve
    if grid[row][col] >0:
        #therefore we moving to the next position
        return solve(grid, row, col+1)

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            # since is passed from above there we are setting the number at that position 
            grid[row][col] = num

            # checkin if we are at the end. and if we are we will return True.
            if solve(grid, row, col+1):
                return True

        # if not valid move is found   
        grid[row][col] = 0

    return False # this no possible solution for this field


grid = [[0, 0, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 0, 0, 7, 3, 0, 0, 9],
        [3, 0, 9, 0, 0, 0, 0, 4, 5],
        [4, 9, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 5, 0, 9, 0, 2], 
        [0, 0, 0, 0, 0, 0, 0, 3, 6],
        [9, 6, 0, 0, 0, 0, 3, 0, 8],
        [7, 0, 0, 6, 8, 0, 0, 0, 0],
        [0, 2, 8, 0, 0, 0, 0, 0, 0]]

if solve(grid, 0 , 0):
    #print the solved grid
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()

# if no solution is found:
else:
    print("No solution for this sudoku grid")
