import globales, random

productos = [
    "Café Americano",
    "Té Chai",
    "Croissant",
    "Jugo Naranja",
    "Panini de Pavo y Queso",
    "Pastel de Zanahoria",
    "Espresso Doble",
    "Batido de Frutas",
    "Muffin",
    "Ensalada",
    "Chocolate Caliente",
    "Tarta de Frambuesa",
    "Sándwich de Huevo",
    "Galletas de Avena",
    "Frappé de Caramelo"
]

def asignar_montos():
    todos_los_productos = globales.leer_archivo_json('productos.json')

    for producto in productos:
        monto = random.randint(20,100)*100

        nuevo_producto = {
            "nombre": producto,
            "valor": monto,
            "iva": int(monto*0.19)
        }

        todos_los_productos.append(nuevo_producto)
    
    globales.guardar_archivo_json('productos.json', todos_los_productos)

    