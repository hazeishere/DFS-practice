def print_island(grid):
    for row in grid:
        print(" ".join(map(str, row)))
    print()

def num_islands(grid):
    """
    Count the number of islands in a 2D grid.
    
    Args:
        grid: 2D list where 1 represents land and 0 represents water
        
    Returns:
        int: The number of islands
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r, c):
        # Check if position is out of bounds or is water (0)
        if (r < 0 or r >= rows or
            c < 0 or c >= cols or
            grid[r][c] == 0):
            return
        
        # Mark as visited by changing to 0
        grid[r][c] = 0
        
        # Explore all four directions
        dfs(r+1, c)  # down
        dfs(r-1, c)  # up
        dfs(r, c+1)  # right
        dfs(r, c-1)  # left
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                count += 1  # Found a new island
                dfs(r, c)   # Explore the island and mark all its cells
    
    return count

# Example test cases
if __name__ == "__main__":
    grid1 = [
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    print("Number of islands in grid1:")
    print_island(grid1)
    print(num_islands(grid1))
    
    grid2 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]
    print("Number of islands in grid2:")
    print_island(grid2)
    print(num_islands(grid2))
