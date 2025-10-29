import sys
from collections import deque

COLORS = {
    "RED": "\033[91m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "RESET": "\033[0m"
}

def load_maze(filename):

        with open(filename, "r") as f:
            return f.read().splitlines()
  

def find_char(maze, char_to_find):

    for r, row in enumerate(maze):
        for c, char in enumerate(row):
            if char == char_to_find:
                return (r, c)
    return None

def get_neighbors(maze, node):

    r, c = node
    directions = [
        (r - 1, c),  
        (r + 1, c),  
        (r, c - 1),  
        (r, c + 1)   
    ]
    
    max_rows = len(maze)
    max_cols = len(maze[0])
    
    neighbors = []
    for nr, nc in directions:
        if 0 <= nr < max_rows and 0 <= nc < max_cols:
            if maze[nr][nc] != '#':
                neighbors.append((nr, nc))
    return neighbors

def solve(maze, start, target, algorithm):

    if algorithm == 'bfs':
        frontier = deque([start])
        pop_method = frontier.popleft
    elif algorithm == 'dfs':
        frontier = [start]
        pop_method = frontier.pop
    else:
        return None 

    visited = {start}
    parent_map = {start: None} 

    while frontier:
        current_node = pop_method()

        if current_node == target:
            return parent_map 

        for neighbor in get_neighbors(maze, current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                parent_map[neighbor] = current_node
                frontier.append(neighbor)
    
    return None 

def print_solution(maze, start, target, parent_map):
   

    path = set()
    current = target
    while current is not None:
        path.add(current)
        current = parent_map.get(current) 

    maze_lists = [list(row) for row in maze]

    for r, c in path:
        if (r, c) != start and (r, c) != target:
            maze_lists[r][c] = '*'

    for r, row in enumerate(maze_lists):
        output_line = ""
        for c, char in enumerate(row):
            pos = (r, c)
            if pos == start:
                output_line += f"{COLORS['YELLOW']}S{COLORS['RESET']}"
            elif pos == target:
                output_line += f"{COLORS['GREEN']}T{COLORS['RESET']}"
            elif char == '*':
                output_line += f"{COLORS['RED']}*{COLORS['RESET']}"
            else:
                output_line += char
        print(output_line)


def main():
        
    algorithm = sys.argv[1].lower()
    filename = sys.argv[2]
    
    maze_data = load_maze(filename)

    start_pos = find_char(maze_data, 'S')
    target_pos = find_char(maze_data, 'T')
    
    parent_map = solve(maze_data, start_pos, target_pos, algorithm)

    print_solution(maze_data, start_pos, target_pos, parent_map)


if __name__ == "__main__":
    main()