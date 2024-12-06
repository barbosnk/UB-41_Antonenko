def is_magic_square(matrix):

    n = len(matrix)
    """#проверка на магический квадрат"""
    if n == 0 or len(matrix[0]) != n :
        return False
    """isinstance  - это проверка типа данных""" """#сумма строки"""
    if not all(isinstance(x, (int,float)) for row in matrix for x in row):
        return False
    row_sum = sum(matrix[0])

    for i in range(n):
        """#проверка суммы"""
        if sum(matrix[i]) != row_sum:
            return False
        """#cymma vsex elementov ctroki"""
        col_sum = sum(matrix[j][i] for j in range(n))
        if col_sum != row_sum:
            return False
    return True

square = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

print(f'Это магическая матрица: {is_magic_square(square)}', '\n', square)