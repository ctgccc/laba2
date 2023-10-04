def count_nonzero_columns():
    m = int(input("Введите количество строк матрицы: "))
    n = int(input("Введите количество столбцов матрицы: "))

    if m == n:
        print("Неверная размерность матрицы!")
        return

    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            num = int(input(f"Введите элемент [{i}][{j}]: "))
            row.append(num)
        matrix.append(row)

    nonzero_cols = 0
    for j in range(n):
        has_zero = False
        for i in range(m):
            if matrix[i][j] == 0:
                has_zero = True
                break
        if not has_zero:
            nonzero_cols += 1

    print(f"Количество столбцов, не содержащих ни одного нулевого элемента: {nonzero_cols}")

count_nonzero_columns()
