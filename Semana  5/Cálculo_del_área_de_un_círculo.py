# Importar la librería matemática para usar PI
"""
# Programa en Python para calcular el área de un círculo.
# El usuario ingresa el radio, y el programa valida el dato,
# calcula el área utilizando la fórmula matemática (π * r^2)
# y muestra el resultado redondeado a dos decimales.
"""

import math


def calcular_area_circulo(radio: float) -> float:
    """
    Calcula el área de un círculo dado su radio.

    """
    area = math.pi * radio ** 2
    return area


# Iniciar el programa
print("=== CÁLCULO DEL ÁREA DE UN CÍRCULO ===")

# Entrada del usuario (tipo string convertida a float)
entrada_radio = input("Ingrese el radio del círculo en cm: ")
radio_circulo = float(entrada_radio)

# Validación (tipo boolean)
es_valido = radio_circulo > 0

if es_valido:
    # Llamar a la función
    area_resultado = calcular_area_circulo(radio_circulo)

    # Mostrar resultado (con redondeo)
    print(f"El área del círculo con radio {radio_circulo} cm es {round(area_resultado, 2)} cm²")
else:
    print("El valor ingresado no es válido. El radio debe ser mayor que cero.")
