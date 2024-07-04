import globales, math

# lambda x:x [variable], reverse=True

def producto_valor_mas_alto():
    todos_los_productos = globales.leer_archivo_json('productos.json')

    productos_ordenados = sorted(todos_los_productos, key=lambda x:x["valor"], reverse= True)

    print("| Producto           | Valor    |")
    for producto in productos_ordenados[:1]:
        nombre = producto["nombre"]
        valor = producto["valor"]
        print(f"| {nombre:19}| {valor:9}|")


def producto_iva_mas_bajo():
    todos_los_productos = globales.leer_archivo_json('productos.json')

    productos_ordenados = sorted(todos_los_productos, key=lambda x:x["iva"], reverse= False)

    print("| Producto           | IVA      |")
    for producto in productos_ordenados[:1]:
        nombre = producto["nombre"]
        iva = producto["iva"]
        print(f"| {nombre:19}| {iva:9}|")

def promedio_valores():
    todos_los_productos = globales.leer_archivo_json('productos.json')

    suma_valores = 0
    cantidad_valores = 0

    for producto in todos_los_productos:
        suma_valores += producto["valor"]
        cantidad_valores += 1

    promedio = int(suma_valores/cantidad_valores)

    print(f"El promedio del valor de los productos es de ${promedio}")

def media_geometrica():
    todos_los_productos = globales.leer_archivo_json('productos.json')

    suma_valores = 0
    cantidad_valores = 0

    for producto in todos_los_productos:
        suma_valores += math.log(producto["valor"])
        cantidad_valores += 1

    media = int(math.exp(suma_valores/cantidad_valores))

    print(f"La media geometrica del valor de los productos es de ${media}")
