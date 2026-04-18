#PROYECTO DE PROGRAMADOR - NIVEL 1

nombre_producto = "cemento avellenada x 50kg"
stock_disponible = 120
precio_lista = 8500
es_importado = False
#calculamos el valor total
valor_total = stock_disponible * precio_lista

#mostramos el reporte en consola
print("-- REPORTE DE INVENTARIO EDF --")
print("producto:", nombre_producto)
print("valor total en deposito: $", valor_total)
print("-----------------------")
proveedor = "cementos avellaneda"
impuesto_iva = 1.21

precio_con_iva = precio_lista * impuesto_iva
print("precio oficial:", proveedor)
print("precio unitario con iva: $", precio_con_iva)

