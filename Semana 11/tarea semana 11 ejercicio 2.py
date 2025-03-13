# Crear la matriz bidimensional (3x3)
matriz = [
    [5, 4, 3],
    [6, 7, 8],
    [2, 1, 9],
]

# Valor que estamos buscando
valor_buscado = 7

# Inicializar variables para rastrear la posición del valor
fila_encontrada = -1
columna_encontrada = -1

# Recorrer la matriz para buscar el valor
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break  # Detener la búsqueda una vez que se encuentre el valor
    if fila_encontrada != -1:  # Salir del bucle exterior si se encuentra el valor
        break

# Verificar si se encontró el valor y mostrar la posición
if fila_encontrada != -1:
    print(f"Se encontró el valor {valor_buscado} en la posición ({fila_encontrada}, {columna_encontrada}).")
else:
    print(f"El valor {valor_buscado} no se encuentra en la matriz.")
