import os, productos, estadisticas, globales

def menu_estadisticas():
    while True:
        os.system("cls")
        print("== Estadisticas ==")
        print("1. Producto con valor más alto")
        print("2. Producto con valor del IVA más bajo.")
        print("3. Promedio del valor de los productos.")
        print("4. Media geométrica del valor de los productos.")
        print("5. Regresar")

        opcion = globales.seleccionar_opcion(5)

        if opcion == 1:
            estadisticas.producto_valor_mas_alto()
            input("Enter para continuar")
        elif opcion == 2:
            estadisticas.producto_iva_mas_bajo()
            input("Enter para continuar")
        elif opcion == 3:
            estadisticas.promedio_valores()
            input("Enter para continuar")
        elif opcion == 4:
            estadisticas.media_geometrica()
            input("Enter para continuar")
        elif opcion == 5:
            return False

def menu_ppal():
    while True:
        os.system("cls")
        print("== Menu Principal ==")
        print("1. Asignar montos aleatorios.")
        print("2. Ver estadísticas.")
        print("3. Salir del programa.")

        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            productos.asignar_montos()
            input("Montos Asignados")
        elif opcion == 2:
            menu_estadisticas()
        elif opcion == 3:
            print("Adios")
            return False
    

if __name__ == "__main__":
    menu_ppal()
