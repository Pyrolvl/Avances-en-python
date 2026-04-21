# 1. Creamos la "máquina" de saludar clientes
def saludar_cliente(nombre):
    print(f"¡Hola {nombre}! Bienvenido a EDF Materiales.")
    print("¿En qué podemos ayudarte hoy?")
    print("--------------------------------")

# 2. Ahora la usamos con distintos clientes
saludar_cliente("Nolberto")
saludar_cliente("Juan")


def despedir_cliente(nombre):
    print(f"¡Gracias por tu visita, {nombre}! Esperamos verte pronto.")
    print("¡Que tengas un excelente día!")
    print("--------------------------------")
despedir_cliente("Nolberto")
