
def calcular_total(precio, cantidad):
    return precio * cantidad


def aplicar_descuento(subtotal):
    if subtotal >= 200:
        return subtotal * 0.90
    return subtotal


# Datos de la venta
precio = 50
cantidad = 4

# Calcular subtotal y descuento
subtotal = calcular_total(precio, cantidad)
total = aplicar_descuento(subtotal)

print("Subtotal: S/", subtotal)
print("Total: S/", total)
