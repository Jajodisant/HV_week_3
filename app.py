# Importo funciones de otros archivos
# 'archivo' tiene las funciones para guardar y cargar el inventario en CSV
# 'servicios' tiene funciones para manejar los productos (agregar, actualizar, mostrar, eliminar, etc.)
from archivo import guardar_inventario, cargar_inventario
from servicios import agregar_producto, actualizar_producto, mostrar_productos, eliminar_producto, calcular_estadisticas, buscar_producto

# Creo la lista que va a almacenar todos los productos del inventario
lista_inventario = []   # <-- Aquí guardo mis productos

# Variable que me va a permitir mantener el menú abierto hasta que decida salir
menu = True

# Empiezo el ciclo del menú principal
while menu:
    # Muestro todas las opciones disponibles para el usuario
    print("    1. Agregar producto\n\
    2. Mostrar inventario\n\
    3. Buscar producto\n\
    4. Actualizar producto\n\
    5. Eliminar Producto\n\
    6. Calcular estadísticas\n\
    7. Guardar el inventario en un CSV\n\
    8. Fusionar o Sobrescribir el CSV del inventario\n\
    9. SALIR")

    # Le pido al usuario que ingrese la opción que desea realizar
    opcion = input("\nQué acción desea realizar: ")

    # Valido que lo ingresado sea un número, no quiero que ponga texto
    if not opcion.isdigit():
        print(">>>Error! NO se admite texto!\n")
        continue  # Si no es número, vuelvo a mostrar el menú

    # Convierto la opción a número entero para poder usarla en los if
    opcion = int(opcion)

    # Verifico que la opción esté dentro del rango permitido (1-9)
    if opcion < 1 or opcion > 9:
        print(">>>Error! Ingresa una opción valida!\n")
        continue  # Si no es válida, vuelvo a mostrar el menú

    # -------------------- OPCIÓN 1 --------------------
    if opcion == 1:
        print("\nAGREGAR PRODUCTOS")

        # Uso un ciclo para permitir que el usuario agregue varios productos seguidos
        while True:
            # Pido los datos del producto al usuario
            nombre = input("Ingresa el nombre del producto: ")
            precio = float(input("Ingresa el precio del producto: "))
            cantidad = int(input("Ingresa la cantidad del producto: "))

            # Creo un diccionario con los datos ingresados
            producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}

            # Llamo a la función que agrega el producto a mi lista de inventario
            agregar_producto(lista_inventario, producto)

            # Pregunto si el usuario quiere seguir agregando productos
            while True:
                opcion_continuar = input("¿Quieres seguir agregando productos? (s/n): ").lower()

                if opcion_continuar == "s":
                    continuar = True  # Si dice "s", seguimos agregando
                    break

                elif opcion_continuar == "n":
                    continuar = False  # Si dice "n", salgo del ciclo
                    break

                elif opcion_continuar.isdigit():
                    # No permito números en esta pregunta
                    print(">>>Opción incorrecta, no se admiten números")

                else:
                    # Cualquier otro ingreso que no sea "s" o "n" lo rechazo
                    print(">>>Opción incorrecta, ingresa 's' o 'n'")

            # Si el usuario no quiere continuar, salgo del ciclo de agregar productos
            if not continuar:
                break

    # -------------------- OPCIÓN 2 --------------------
    elif opcion == 2:
        print("\nINVENTARIO ACTUAL")
        # Llamo a la función que muestra todos los productos del inventario
        mostrar_productos(lista_inventario)

    # -------------------- OPCIÓN 3 --------------------
    elif opcion == 3:
        print("\nBUSCAR PRODUCTOS")
        # Le pido al usuario el nombre del producto a buscar
        nombre = input("Ingresa un producto: ")
        # Muestro el resultado de la búsqueda
        print(buscar_producto(lista_inventario, nombre))

    # -------------------- OPCIÓN 4 --------------------
    elif opcion == 4:
        print("\nACTUALIZAR PRODUCTO")
        # Pido el nombre del producto a actualizar
        nombre = input("Ingresa un producto: ")
        # Pido el nuevo precio y la nueva cantidad
        nuevo_precio = input("Ingresa un nuevo precio: ")
        nueva_cantidad = input("Ingresa un nueva cantidad: ")
        # Llamo a la función que actualiza el producto y muestro el resultado
        print(actualizar_producto(lista_inventario, nombre, nuevo_precio, nueva_cantidad))

    # -------------------- OPCIÓN 5 --------------------
    elif opcion == 5:
        print("\nELIMINAR PRODUCTO")
        # Pido el nombre del producto a eliminar
        nombre = input("Ingresa un producto a eliminar: ")
        # Llamo a la función que elimina el producto y muestro el resultado
        print(eliminar_producto(lista_inventario, nombre))

    # -------------------- OPCIÓN 6 --------------------
    elif opcion == 6:
        print("\nESTADISTICAS")
        # Llamo a la función que calcula estadísticas del inventario y las muestro
        print(calcular_estadisticas(lista_inventario))

    # -------------------- OPCIÓN 7 --------------------
    elif opcion == 7:
        # Llamo a la función que guarda mi inventario en un CSV
        guardar_inventario(lista_inventario)

    # -------------------- OPCIÓN 8 --------------------
    elif opcion == 8:
        # Llamo a la función que carga un CSV en mi inventario
        # Por defecto uso sobrescribir, también podría usar fusionar
        cargar_inventario(lista_inventario, opcion="sobrescribir")

    # -------------------- OPCIÓN 9  -------------------
    elif opcion == 9:
        # Salgo del programa mostrando un mensaje de despedida
        print(">>> FIN DEL PROGRAMA <<<")
        break
