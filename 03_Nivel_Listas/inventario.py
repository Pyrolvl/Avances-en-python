# --- NIVEL 3: MANEJO DE LISTAS EN EDF ---

# 1. Creamos el catálogo inicial (nuestra "estantería")
productos = ["Cemento", "Cal", "Arena", "Ladrillos", "Hierro"]

# 2. Llegó un producto nuevo (usamos .append)
productos.append("Chapa C-25")
productos.append("Hidrofugo")
# 3. Nos dimos cuenta que 'Arena' era muy genérico, lo cambiamos por 'Arena Fina'
# Recordá: Python cuenta 0 (Cemento), 1 (Cal), 2 (Arena)...
productos[2] = "Arena Fina"
productos[5] = "Hidrofugo Holcim"

# --- REPORTE DE STOCK ---
print("--- STOCK ACTUALIZADO EDF ---")
print("Lista completa:", productos)
print("En total tenemos", len(productos), "variedades de artículos.")

# 4. Acceder al último producto de forma inteligente
print("🚀 El último ingreso al corralón fue:", productos[-1])