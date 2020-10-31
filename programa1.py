

precio = 120

if precio > 100:
    precio = 0.9*precio
print(precio)
precio = 120
if precio < 120:
    precio = precio*.9

print(precio) 

def descuento(total):
    if total > 100:
        return total*0.9
    return total

print(descuento(500))