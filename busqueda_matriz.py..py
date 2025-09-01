matriz = [
    [5, 8, 2],
    [4, 7, 1],
    [9, 6, 3]
]

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición (fila, columna)
    return None  # Si no se encuentra

valor = int(input("Ingresa el valor a buscar: "))

resultado = buscar_valor(matriz, valor)

if resultado:
    print(f"Valor {valor} encontrado en la posición: {resultado}")
else:
    print(f"Valor {valor} no encontrado en la matriz.")

