import math
import logic
import grid
from grid import board

def minimax(board, depth, maximizing_player, alpha, beta):
    """
    Minimax algorithm with alpha-beta prune
        board (list): The 4x4x4 game board as a 3D list.
        depth (int): The depth of the search tree.
        maximizing_player (bool): True if it's the AI's turn, False for opponent.
        alpha (float): Alpha value for pruning.
        beta (float): Beta value for pruning.

    """
    if depth == 0 or is_terminal(board):
        return evaluate_board(board), None

    best_move = None
    if maximizing_player:
        max_eval = -math.inf
        for layer, row, col in generate_legal_moves(board):
            grid.update_grid(board, layer, row, col, 1)  # AI's move 1 represents AI
            eval_score, _ = minimax(board, depth - 1, False, alpha, beta)
            undo_move(board, layer, row, col)  # Undo the move
            
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = layer, row, col
            
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval, best_move
    else:
        min_eval = math.inf
        for layer, row, col in generate_legal_moves(board):
            grid.update_grid(board, layer, row, col, 2) # Opponent's move 2 represents opponent
            eval_score, _ = minimax(board, depth - 1, True, alpha, beta)
            undo_move(board, layer, row, col)  # Undo the move
            
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = layer, row, col
            
            beta = min(beta, eval_score)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval, best_move


def evaluate_board(board):
    
    # Evaluate the board and return a heuristic score.
    score = 0

    # Define weights for different line completions
    WINNING_SCORE = 1000
    THREE_IN_A_ROW = 100
    TWO_IN_A_ROW = 10

    # Iterate through all possible lines (rows, columns, diagonals)
    for line in logic.get_all_lines(board):  # Implement `logic.get_all_lines` to return all possible lines
        ai_count = line.count(1)
        opponent_count = line.count(2)
        empty_count = line.count(0)

        if ai_count == 4:  # AI wins
            return WINNING_SCORE
        elif opponent_count == 4:  # Opponent wins
            return -WINNING_SCORE

        # Heuristic for partial lines
        if ai_count == 3 and empty_count == 1:
            score += THREE_IN_A_ROW
        elif ai_count == 2 and empty_count == 2:
            score += TWO_IN_A_ROW

        if opponent_count == 3 and empty_count == 1:
            score -= THREE_IN_A_ROW
        elif opponent_count == 2 and empty_count == 2:
            score -= TWO_IN_A_ROW

    return score

def is_terminal(board):
    # Check for win or loss
    for line in logic.get_all_lines(board):
        if line.count(1) == 4 or line.count(2) == 4:
            return True
    # Check if the board is full
    grid.grid_status(board)

def generate_legal_moves(board):

    # Generate all legal moves on the board.
    legal_moves = []  # Initialize an empty list to store legal moves
    for layer in range(4):
        for row in range(4):
            for col in range(4):
                if logic.legal_move(board, layer, row, col):  # Check if the move is legal
                    legal_moves.append((layer, row, col))  # Add the move to the list
    return legal_moves  # Return the list of all legal moves

# print(generate_legal_moves(board))

def undo_move(board, layer, row, col):

    # Undo a move on the board.

    board[layer][row][col] = 0  # Reset to empty


score, move = minimax(board,3,True, -math.inf, math.inf)
print(f"Best Move: {move}, Score: {score}")