def pascal_triangle(n):
    """Return a list of lists of integers representing the Pascal's triangle of n."""
    if n <= 0:
        return []
    else:
        triangle = []
        for i in range(n):
            row = [1]
            if triangle:
                last_row = triangle[-1]
                row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
                row.append(1)
            triangle.append(row)
        return triangle