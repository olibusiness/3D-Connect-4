
def create_rest_grid():
        # Create a 4x4x4 grid filled with zeros
    board = [[[0 for col in range(4)] for col in range(4)] for row in range(4)]
    
    # layer, row, column
    # board[0][0][0] = 1  # Separate layers for readability
    # board[0][1][0] = 1 
    # board[0][2][0] = 1 
    # board[0][3][0] = 1 
    return board

def grid_status(grid):
    total = 0
    for layer in grid:
        for row in layer:
            for cell in row:
                if cell == 0:
                    total += 1
    if total != 0:
        return False
    else:
        return True
         
        

def update_grid(grid, layer, row, col, value):
    # Updates the grid at the specified layer, row, and column with the given value.
    
    grid[layer][row][col] = value
    

board = create_rest_grid()
