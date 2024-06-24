#!/usr/bin/python3
''' solving the island perimeter problem '''


def island_perimeter(grid):
    # Initialize perimeter
    perimeter = 0
    # Get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Traverse the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Each land cell can contribute up to 4 to the perimeter
                # Check all four sides
                if r == 0 or grid[r-1][c] == 0:  # check upwards
                    perimeter += 1
                if r == rows-1 or grid[r+1][c] == 0:  # check downwards
                    perimeter += 1
                if c == 0 or grid[r][c-1] == 0:  # check leftwards
                    perimeter += 1
                if c == cols-1 or grid[r][c+1] == 0:  # check rightwards
                    perimeter += 1
    return perimeter
