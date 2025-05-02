# Depth-First Search (DFS) Applications

This repository contains three Python implementations that demonstrate the Depth-First Search algorithm applied to different problems:

## Files Overview

- **app.py**: Maze solver - finds a path through a maze using DFS
- **app2.py**: Island counter - counts isolated islands in a 2D grid
- **app3.py**: Word search - determines if a word exists in a 2D board of characters

## What is Depth-First Search (DFS)?

Depth-First Search is a graph traversal algorithm that explores as far as possible along each branch before backtracking. When implemented recursively, DFS uses the call stack to keep track of vertices to be explored.

### How DFS Works

1. Start at a source vertex (or cell in a 2D grid)
2. Mark the current vertex as visited
3. Recursively explore all adjacent unvisited vertices
4. Backtrack when no unvisited adjacent vertices remain

### Key Properties of DFS

- **Time Complexity**: O(V + E) for a graph with V vertices and E edges
- **Space Complexity**: O(V) for the recursive call stack
- **Traversal Pattern**: Goes deep before going wide

## When to Use DFS

DFS is particularly useful for:

- Finding paths in mazes or grids
- Topological sorting
- Detecting cycles in graphs
- Connected components
- Solving puzzles with backtracking
- Tree/graph traversal where you want to explore completely down one path

## Examples in This Repository

### 1. Maze Solver (app.py)

Demonstrates how DFS can be used to find a path from a start point to an end point in a maze.

- Uses backtracking to explore possible paths
- Marks visited cells to avoid cycles
- Returns the complete path when found

### 2. Island Counter (app2.py)

Counts the number of isolated "islands" in a 2D grid where:
- 1 represents land
- 0 represents water

The algorithm:
- Scans the grid to find unvisited land cells
- For each land cell found, performs DFS to mark the entire island as visited
- Counts each isolated island once

### 3. Word Search (app3.py)

Determines if a word can be constructed from a 2D board of characters by:
- Searching for the first letter of the word in the board
- Using DFS to explore adjacent cells for subsequent letters
- Preventing the reuse of cells by temporarily marking them
- Backtracking when a path doesn't lead to a complete word

## How to Run the Examples

```bash
# Run the maze solver
python dfs_prac/app.py

# Run the island counter
python dfs_prac/app2.py

# Run the word search
python dfs_prac/app3.py
```

## DFS vs BFS

While this repository focuses on DFS, it's worth comparing it to Breadth-First Search (BFS):

- **DFS**: Goes deep first, uses less memory for sparse graphs, good for finding paths that might exist far from the source
- **BFS**: Explores all neighbors before going deeper, finds shortest paths, better for dense graphs or when the solution is likely near the starting point 