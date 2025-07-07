import random
# Función para calcular el descuento de un producto
def calcular_descuento(precio_original, porcentaje_descuento):
    if not isinstance(precio_original, (int, float)) or precio_original < 0:
        raise ValueError("El precio original debe ser un número positivo.")

    if not isinstance(porcentaje_descuento, (int, float)) or porcentaje_descuento < 0 or porcentaje_descuento > 100:
        raise ValueError("El porcentaje de descuento debe ser un número entre 0 y 100.")

    descuento = precio_original * (porcentaje_descuento / 100)
    precio_final = precio_original - descuento
    return precio_final


# Menú de ejemplo (no funcional, solo decorativo)
def mostrar_menu():
    print("Seleccione una opción de conversión:")
    print("1. Grados Celsius a Fahrenheit")
    print("2. Metros a pies")
    print("3. Salir")


# Ejecución principal
if __name__ == "__main__":
    try:
        # Generar precio aleatorio entre 10 y 500
        precio_producto = round(random.uniform(10, 500), 2)

        # Generar porcentaje aleatorio entre 5% y 50%
        porcentaje = round(random.uniform(5, 50), 2)

        precio_con_descuento = calcular_descuento(precio_producto, porcentaje)

        # Mostrar resultados
        print("=== Cálculo de Descuento ===")
        print(f"Precio original: ${precio_producto:.2f}")
        print(f"Descuento aplicado: {porcentaje}%")
        print(f"Precio final con descuento: ${precio_con_descuento:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
