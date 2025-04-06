# Escritura en el archivo 'my_notes.txt'
# Abrimos el archivo en modo de escritura ('w'). Si el archivo no existe, se creará.

with open('my_notes.txt', 'w') as archivo:
    archivo.write("Primera nota personal: Estudiar para el examen de matemáticas.\n")
    archivo.write("Segunda nota personal: Terminar el proyecto de Python.\n")
    archivo.write("Tercera nota personal: Llamar a los padres para saber cómo están.\n")
    # El archivo se cierra automáticamente al salir del bloque 'with'

# Lectura del archivo 'my_notes.txt'
# Abrimos el archivo en modo de lectura ('r') para leer su contenido.

with open('my_notes.txt', 'r') as archivo:
    # Leemos línea por línea
    for linea in archivo:
        print(linea.strip())  # Utilizamos 'strip()' para eliminar los saltos de línea

# El archivo se cierra automáticamente al salir del bloque 'with'
