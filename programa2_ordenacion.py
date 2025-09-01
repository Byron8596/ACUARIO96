
def bubble_sort_row(matrix, row_index):
    n = len(matrix[row_index])
    for i in range(n):
        for j in range(0, n-i-1):
            if matrix[row_index][j] > matrix[row_index][j+1]:
                matrix[row_index][j], matrix[row_index][j+1] = matrix[row_index][j+1], matrix[row_index][j]
    return matrix

# Matriz inicial 3x3
matriz = [
    [9, 3, 7],
    [2, 8, 1],
    [6, 4, 5]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenamos la segunda fila (índice 1)
matriz_ordenada = bubble_sort_row([fila[:] for fila in matriz], 1)

print("\nMatriz con la fila 2 ordenada:")
for fila in matriz_ordenada:
    print(fila)
