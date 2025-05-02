def print_maze(maze):
    for row in maze:
        print(" ".join(map(str, row)))
    print()

def dfs(maze, start, end, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    
    # Current position
    row, col = start
    
    # Check if out of bounds or hitting a wall or already visited
    if (row < 0 or row >= len(maze) or 
        col < 0 or col >= len(maze[0]) or 
        maze[row][col] == 1 or 
        (row, col) in visited):
        return False
    
    # Add current position to path and mark as visited
    path.append((row, col))
    visited.add((row, col))
    
    # If we've reached the end, we're done
    if (row, col) == end:
        return True
    
    # Try all four directions (up, right, down, left)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if dfs(maze, (new_row, new_col), end, path, visited):
            return True
    
    # If no direction leads to the end, backtrack
    path.pop()
    return False

def solve_maze(maze, start, end):
    path = []
    if dfs(maze, start, end, path):
        # Mark the path in the maze with 'P'
        solution = [row[:] for row in maze]
        for r, c in path:
            solution[r][c] = 'P'
        return solution, path
    return None, []

def main():
    # Define a sample maze (0 = path, 1 = wall)
    maze = [
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0]
    ]
    
    start = (0, 0)  # Starting position (top-left)
    end = (4, 4)    # Target position (bottom-right)
    
    print("Original Maze:")
    print_maze(maze)
    
    solution, path = solve_maze(maze, start, end)
    
    if solution:
        print("Path found!")
        print("Solution:")
        print_maze(solution)
        print(f"Path: {path}")
    else:
        print("No path found!")

if __name__ == "__main__":
    main()
