# Definimos la función con dos parámetros
def crear_presupuesto(producto, precio_base):
    # Lógica que se repite siempre
    iva = precio_base * 0.21
    total = precio_base + iva
    
    # Resultado elegante
    print(f"📄 PRESUPUESTO EDF - {producto}")
    print(f"💵 Subtotal: ${precio_base}")
    print(f"🏦 IVA (21%): ${iva}")
    print(f"🛍️ TOTAL A PAGAR: ${total}")
    print("-" * 35)

def crear_presupuesto(producto, precio_base):
    # Lógica que se repite siempre
    iva  = precio_base * 0.21
    total = precio_base + iva
    
    # Resultado elegante
    print(f"📄 PRESUPUESTO EDF - {producto}")
    print(f"💵 Subtotal: ${precio_base}")
    print(f"🏦 IVA (21%): ${iva}")
    print(f"🛍️ TOTAL A PAGAR: ${total}")
    print("-" * 35)

def crear_presupuesto(producto, precio_base):
    # Lógica que se repite siempre
    iva = precio_base * 0.21
    
    total = precio_base + iva
    
    # Resultado elegante
    print(f"📄 PRESUPUESTO EDF - {producto}")
    print(f"💵 Subtotal: ${precio_base}")
    print(f"🏦 IVA (21%): ${iva}")
    print(f"🛍️ TOTAL A PAGAR: ${total}")
    print("-" * 35)

    # Aquí es donde ocurre la magia: rellenamos los huecos
crear_presupuesto("Hierro del 8", 12000)
crear_presupuesto("Malla Simap", 25000)
crear_presupuesto("Bolsa de Cal", 4500)
