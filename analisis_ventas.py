# 1. Lista de Ventas Original
ventas = [
    {"fecha": "2024-01-01", "producto": "Laptop", "cantidad": 2, "precio": 1500.0},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 25.0},
    {"fecha": "2024-01-02", "producto": "Teclado", "cantidad": 3, "precio": 45.0},
    {"fecha": "2024-01-02", "producto": "Laptop", "cantidad": 1, "precio": 1550.0},
    {"fecha": "2024-01-03", "producto": "Mouse", "cantidad": 7, "precio": 24.5},
    {"fecha": "2024-01-03", "producto": "Teclado", "cantidad": 4, "precio": 47.0},
    {"fecha": "2024-01-03", "producto": "Monitor", "cantidad": 2, "precio": 300.0},
]

# 2. Cálculo de Ingresos Totales
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

# 3. Análisis del Producto Más Vendido
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    ventas_por_producto[producto] = ventas_por_producto.get(producto, 0) + cantidad

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]

# 4. Promedio de Precio por Producto
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    ingreso = venta["cantidad"] * venta["precio"]
    cantidad = venta["cantidad"]
    if producto not in precios_por_producto:
        precios_por_producto[producto] = (0.0, 0)
    suma, total = precios_por_producto[producto]
    precios_por_producto[producto] = (suma + ingreso, total + cantidad)

precio_promedio_por_producto = {
    producto: round(suma / total, 2)
    for producto, (suma, total) in precios_por_producto.items()
}

# 5. Ventas por Día
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    ingresos_por_dia[fecha] = ingresos_por_dia.get(fecha, 0) + ingreso

# 6. Resumen de Ventas por Producto
resumen_ventas = {}
for producto in ventas_por_producto:
    cantidad_total = ventas_por_producto[producto]
    ingresos_totales_producto, _ = precios_por_producto[producto]
    precio_promedio = precio_promedio_por_producto[producto]
    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": round(ingresos_totales_producto, 2),
        "precio_promedio": precio_promedio
    }

# 7. Resultados
print("\n--- LISTA DE VENTAS ---")
for v in ventas:
    print(v)

print("\n✅ Ingresos Totales:", round(ingresos_totales, 2))

print("\n📦 Producto más vendido:", producto_mas_vendido)
print("   Cantidad total vendida:", cantidad_mas_vendida)

print("\n💲 Precio promedio de venta por producto:")
for producto, promedio in precio_promedio_por_producto.items():
    print(f" - {producto}: ${promedio}")

print("\n📅 Ingresos totales por día:")
for fecha, ingreso in ingresos_por_dia.items():
    print(f" - {fecha}: ${round(ingreso, 2)}")

print("\n📊 Resumen de ventas por producto:")
for producto, resumen in resumen_ventas.items():
    print(f" - {producto}:")
    for clave, valor in resumen.items():
        print(f"     {clave}: {valor}")
