
def create_rest_grid():
        # Create a 4x4x4 grid filled with zeros
    board = [[[0 for col in range(4)] for col in range(4)] for row in range(4)]
    
    # layer, row, column
    board[0][0][0] = 5  # Separate layers for readability
    board[1][1][1] = 5 
    board[2][0][2] = 5 
    board[3][3][3] = 5 
    return board

def grid_status(grid):
    total = 0
    for layer in grid:
        for row in layer:
            for cell in row:
                if cell == 0:
                    total += 1
    if total != 0:
        return "board not full"
    else:
        return "board full"
         
        

def update_grid():
    pass
    

board = create_rest_grid()
