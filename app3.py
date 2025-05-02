def exist(board, word):
    if not board or not word:
        return False
    
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c, index):
        # Base case: if we've matched all characters in the word
        if index == len(word):
            return True
        
        # Check if current position is out of bounds, or character doesn't match, or cell was visited
        if (r < 0 or r >= rows or
            c < 0 or c >= cols or 
            board[r][c] != word[index] or board[r][c] == '#'):
            return False
        
        # Mark current cell as visited (temporarily)
        temp = board[r][c]
        board[r][c] = '#'  # Use a special character to mark as visited
        
        # Explore in all four directions
        found = (dfs(r+1, c, index+1) or  # Down
                 dfs(r-1, c, index+1) or  # Up
                 dfs(r, c+1, index+1) or  # Right
                 dfs(r, c-1, index+1))     # Left
        
        # Restore the cell (backtrack)
        board[r][c] = temp
        
        return found
    
    # Start DFS from each cell in the board
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True
    
    return False

# Example usage
if __name__ == "__main__":
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    
    print(exist(board, "ABCCED"))  # Output: True
    print(exist(board, "SEE"))     # Output: True
    print(exist(board, "ABCB"))    # Output: False
