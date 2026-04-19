"""
PROYECTO: Sistema de Gestión EDF Materiales
NIVEL 4: Bucles (Loops)
OBJETIVO: Recorrer listas automáticamente.
"""

# Nuestra lista de productos de ayer
productos = ["Cemento", "Cal", "Arena Fina", "Ladrillos", "Hierro", "Viguetas"]

print("--- LISTADO AUTOMÁTICO DE DEPÓSITO ---")

# 'p' es una variable temporal que representa a CADA producto en cada vuelta
for p in productos:
    print("📦 Artículo disponible:", p)

print("--- Fin del reporte ---")

precios = [1000, 2500, 5000]
print("--- PRECIOS DE LOS PRODUCTOS ---")
for i in precios:
    print("💰 Precio:", i, "pesos"  )

for i in precios:
    # creamos el calculo adentro para que se repita con cada numero
    precio_final = i * 1.21
print(f"💰 Precio base: ${i} | Final con IVA: ${precio_final}")

precios = [1000, 2500, 5000]

print("--- CLASIFICACIÓN DE PRECIOS EDF ---")

for i in precios:
    precio_final = i * 1.21
    
    # Aquí tomamos la decisión ADENTRO del bucle
    if precio_final > 3000:
        categoria = "🔴 PRODUCTO PREMIUM"
    else:
        categoria = "🟢 PRODUCTO ACCESIBLE"
        
    print(f"💰 ${precio_final} | {categoria}")