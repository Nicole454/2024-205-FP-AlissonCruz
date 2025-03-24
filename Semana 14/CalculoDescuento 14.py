# Calcular descuento al 10%

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
     Calcula el monto del descuento en función del porcentaje de descuento.
    :param monto_total: float - Monto total sobre el cual aplicar el descuento.
    :param porcentaje_descuento: float - Porcentaje de descuento (por defecto es 10%).
    :return: float - Monto total del descuento.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamadas a la función
monto1 = 650.0
monto2 = 850.0
porcentaje_descuento = 10

descuento1 = calcular_descuento(monto1, porcentaje_descuento)
descuento2 = calcular_descuento(monto2, porcentaje_descuento)

# Cálculo del monto final a pagar
monto_final1 = monto1 - descuento1
monto_final2 = monto2 - descuento2

# Mostrar resultados
print(f'Monto final 1: {monto_final1}')
print(f'Monto final 2: {monto_final2}')
