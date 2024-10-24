from collections import deque

# Get possible moves
def get_moves(x, y):
    return [(x, y), (y, x), (-y, -x), (-x, -y)]

# Check if a move is valid
def is_valid(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0

# BFS function to find the shortest path
def bfs(grid, source, destination, x, y):
    M, N = len(grid), len(grid[0])
    queue = deque([(source[0], source[1], 0)])  # Queue stores (row, col, steps)
    visited = set()
    visited.add((source[0], source[1]))
    moves = get_moves(x, y)
    
    # BFS loop
    while queue:
        row, col, steps = queue.popleft()

        # If destination is reached, return steps
        if (row, col) == (destination[0], destination[1]):
            return steps
        
        # Explore neighbors
        for dx, dy in moves:
            new_row, new_col = row + dx, col + dy
            if is_valid(grid, new_row, new_col) and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, steps + 1))
    
    # Return -1 if no path is found
    return -1

# Input for M and N (dimensions of the grid)
M, N = map(int, input("Enter the dimensions M and N: ").split())

# Input for the grid
print("Enter the grid (0 for free cell, 1 for obstacle):")
grid = [list(map(int, input().split())) for _ in range(M)]

# Input for source and destination (convert to tuples)
source = tuple(map(int, input("Enter the source coordinates (row col): ").split()))
destination = tuple(map(int, input("Enter the destination coordinates (row col): ").split()))

# Input for x and y (the move distances)
x, y = map(int, input("Enter the move distances x and y: ").split())

# Run BFS and print the result
result = bfs(grid, source, destination, x, y)
print("Shortest path steps:", result)