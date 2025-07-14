class Conexion:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Conectado a la base de datos '{self.nombre}'")

    def cambiar_nombre(self, nuevo_nombre):
        print(f"Cambiando el nombre de la base de datos de '{self.nombre}' a '{nuevo_nombre}'")
        self.nombre = nuevo_nombre

    def __del__(self):
        print(f"Conexión con '{self.nombre}' cerrada.")

if __name__ == "__main__":
    c = Conexion("Ventas")
    print("Consultando datos...")
    c.cambiar_nombre("Compras")
    del c
    print("Fin del programa.")
