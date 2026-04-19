

"""

PROYECTO: Sistema de Gestión EDF Materiales

NIVEL 2: Lógica de Ventas y Condicionales

OBJETIVO: Aprender a tomar decisiones automáticas según el pago.

"""



# --- CONFIGURACIÓN DE DATOS (Variables) ---

producto = "Chapa C-25"

precio_lista = 15000

metodo_pago = "tarjeta"  # Opciones: "efectivo" o "tarjeta"



# --- LÓGICA DE NEGOCIO (El "Cerebro") ---

# Si el cliente paga en efectivo, le hacemos un 10% de descuento.

if metodo_pago == "efectivo":

    descuento = precio_lista * 0.10

    precio_final = precio_lista - descuento

    mensaje = "✅ Aplicado descuento del 10% por pago en efectivo."

else:

    precio_final = precio_lista

    mensaje = "ℹ️ Precio de lista (sin descuentos aplicables)."



# --- SALIDA DE DATOS (Lo que ve el usuario) ---

print("---------------------------------------")

print("FACTURACIÓN - EDF MATERIALES")

print("---------------------------------------")

print("Producto:", producto)

print("Estado:", mensaje)

print("Total a cobrar: $", precio_final)

print("---------------------------------------")