#programa 1:Busqueda de una matriz bidimensional

def buscar_valor(matrix, valor):
    """Busca un valor en la matriz y devuelve su posición si se encuentra."""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == valor:
                return i, j
    return None

# Definir una matriz 3x3
matrix = [
    [10, 15, 20],
    [25, 30, 35],
    [40, 45, 50]
]

# Definir el valor a buscar
valor_value = int(input("Ingrese el valor a buscar en la matriz: "))

# Buscar el valor en la matriz
result = buscar_valor(matrix, valor_value)

# Mostrar el resultado
if result:
    print(f"El valor {valor_value} se encontró en la posición {result} (fila {result[0]}, columna {result[1]}).")
else:
    print(f"El valor {valor_value} no se encontró en la matriz.")
