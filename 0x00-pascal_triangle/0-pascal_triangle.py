#!/usr/bin/python3
'''Module to return pascal triangle'''


def pascal_triangle(n):
    '''
    Pascal's triangle
    Args:
      n (int): The number of rows of the triangle
    Returns:
      List of lists of integers representing the Pascal’s triangle
    '''
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
