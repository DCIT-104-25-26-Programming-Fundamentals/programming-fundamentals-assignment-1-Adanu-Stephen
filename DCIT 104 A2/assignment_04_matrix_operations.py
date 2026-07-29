def read_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)

    return matrix


def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)

    return transpose


def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


def multiply_matrices(matrix1, matrix2):
    rows_a = len(matrix1)
    cols_a = len(matrix1[0])
    cols_b = len(matrix2[0])

    result = []

    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix1[i][k] * matrix2[k][j]
            row.append(total)
        result.append(row)

    return result


# ---------------- PART A ----------------

print("PART A - Transpose a Matrix")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = read_matrix(rows, cols)

print("\nOriginal Matrix:")
display_matrix(matrix)

print("\nTransposed Matrix:")
display_matrix(transpose_matrix(matrix))


# ---------------- PART B ----------------

print("\nPART B - Add Two Matrices")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter Matrix A")
matrix1 = read_matrix(rows, cols)

print("Enter Matrix B")
matrix2 = read_matrix(rows, cols)

print("\nMatrix A:")
display_matrix(matrix1)

print("\nMatrix B:")
display_matrix(matrix2)

print("\nSum Matrix:")
display_matrix(add_matrices(matrix1, matrix2))


# ---------------- PART C ----------------

print("\nPART C - Multiply Two Matrices")

rows_a = int(input("Enter rows of Matrix A: "))
cols_a = int(input("Enter columns of Matrix A: "))

print("Enter Matrix A")
matrix1 = read_matrix(rows_a, cols_a)

rows_b = int(input("Enter rows of Matrix B: "))
cols_b = int(input("Enter columns of Matrix B: "))

if cols_a != rows_b:
    print("Matrix multiplication is not possible.")
else:
    print("Enter Matrix B")
    matrix2 = read_matrix(rows_b, cols_b)

    print("\nMatrix A:")
    display_matrix(matrix1)

    print("\nMatrix B:")
    display_matrix(matrix2)

    print("\nProduct Matrix:")
    display_matrix(multiply_matrices(matrix1, matrix2))