"""
Write a function that takes one parameter. The parameter will be a list of lists. Return the elements of the array arranged from outermost elements to the middle element, traveling clockwise. Take a look at the example images for a visual.
"""

def snail(matrix):
    solution = []
    x,y = 0,0
    x_left, y_top= 0,0
    x_right = len(matrix[0]) - 1
    y_bot = len(matrix) - 1

    for i in range(len(matrix[0] * len(matrix))):

        solution.append(matrix[y][x])

        if x < x_right and y == y_top:
            if x == x_left and len(solution) > 1:
                y_bot -= 1
            x += 1
            continue
        if x == x_right and y < y_bot:
            if y == y_top and len(solution) > len(matrix[0]):
                x_left += 1
            y += 1
            continue
        if y == y_bot and x > x_left:
            if x == x_right:
                y_top += 1
            x -= 1
            continue
        if x == x_left and y > y_top:
            if y == y_bot:
                x_right -= 1
            y -= 1
            
    return solution

def test_snail_solution():
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert snail(arr) == expected

    arr = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    expected = [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
    assert snail(arr) == expected

    arr = [
        [1, 2, 3, 4, 5, 6],
        [20, 21, 22, 23, 24, 7],
        [19, 32, 33, 34, 25, 8],
        [18, 31, 36, 35, 26, 9],
        [17, 30, 29, 28, 27, 10],
        [16, 15, 14, 13, 12, 11]
    ]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    assert snail(arr) == expected

