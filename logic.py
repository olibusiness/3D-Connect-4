from grid import board
import grid

# board[1][0][2] = 6
# print(board[1][0][2]) 
# print(grid.grid_status(board))

def check_win(board):
    # Checks all rows
    for layer in range(4):
        for row in range(4):
            first_val = board[layer][row][0]
            if first_val != 0:
                for col in range(4):
                    if board[layer][row][col] != first_val:
                        break  # Exit the loop if a mismatch is found
                else:  
                    return f"Winner found in layer {layer}, row {row}"

    # Checks all col
    for layer in range(4):
        for col in range(4):
            first_val = board[layer][0][col]
            if first_val != 0:
                for row in range(4):
                    if board[layer][row][col] != first_val:
                        break  # Exit the loop if a mismatch is found
                else:  
                    return f"Winner found in layer {layer}, col {col}"
    # vertical check 
    for row in range(4):
        for col in range(4):
            first_val = board[0][row][col]
            if first_val != 0:
                for layer in range(4):
                    if board[layer][row][col] != first_val:
                        break  # Exit the loop if a mismatch is found
                else:  
                    # This else runs only if the 'for' loop completes without 'break'
                    return f"Vertical Winner found in row {row}, col {col}"
    
    # check basic diagonal in each layer 
    for layer in range(4):
        first_val = board[layer][0][0]
        if first_val != 0:
            for i in range(4):
                if board[layer][i][i] != first_val:
                    break
            else:
                return f"Diagonal Winner found in layer {layer}"

    # Check diagonal other direction in each layer 
    for layer in range(4):
        first_val = board[layer][0][3]
        if first_val != 0:
            for i in range(4):
                if board[layer][i][3-i] != first_val:
                    break
            else:
                return f"Diagonal Winner found in layer {layer}"
            
    # Check for diagonals across layers
    for row in range(4):
        first_val = board[0][row][0]
        if first_val != 0:
            for layer_col in range(4):
                if board[layer_col][row][layer_col] != first_val:
                    break
            else:
                return f"3D Diagonal Winner found along row {row} and layers"
            
    # Check for diagonals across layers in the other direction
    for row in range(4):
        first_val = board[0][row][3]  # Start from top-right corner of the first layer
        if first_val != 0:
            for layer_col in range(4):
                if board[layer_col][row][3 - layer_col] != first_val:
                    break
            else:
                return f"3D Diagonal Winner found along row {row} in reverse direction"
    
    # from [0][0][0] to [3][3][3]
    first_val = board[0][0][0]
    if first_val != 0:
        for part in range(4):
            if board[part][part][part] != first_val:
                break
        else: 
            return "3D Diagonal done the middle"

    # from [0][0][3] to [3][3][0]
    first_val = board[0][0][3]
    if first_val != 0:
        for part in range(4):
            if board[part][part][3 - part] != first_val:
                break
        else: 
            return "3D Diagonal done in the other direction"
    
    # from [0][3][0] to [3][0][3]
    first_val = board[0][3][0]
    if first_val != 0:
        for part in range(4):
            if board[part][3-part][part] != first_val:
                break
        else:
            return "3D Diagonal done the middle"

    # from [0][0][3] to [3][3][0]
    first_val = board[0][0][3]  # Initialize once
    if first_val != 0:
        for part in range(4):
            if board[part][part][3 - part] != first_val:
                break
        else:  # Executes only if no break occurs in the loop
            return "3D Diagonal from [0][0][3] to [3][3][0] is done"
        
    return False  # No winner found


# print(check_win(board))  # Output: "Winner found in layer 0, row 0"

# player turns white starts first black after 
def who_move(num_turn):
    if num_turn % 2 == 0:
        return "White"
    else:
        return "Brown"

num_turn = 7
# print(who_move(num_turn)) #keep track of how many moves that returns whos move it is


# what change they want to the board 
def legal_move(board, move):

    layer, row, col = move  # Unpack the move coordinates
    for n in range (layer):
        if board[n][row][col] == 0:
            return "Can't move there"
    else:
        if board[layer][row][col] == 0:
            return "Legit move"
        else:
            return "Can't move there"


print(legal_move(board, [0, 0, 0]))