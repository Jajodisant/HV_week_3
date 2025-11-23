import csv  # Importo la librería csv para poder leer y escribir archivos CSV

# -------------------- FUNCION PARA GUARDAR INVENTARIO --------------------
def guardar_inventario(lista_inventario, archivo="HV_week_3-main\inventario.csv"):
    # Abro el archivo en modo escritura ('w'), uso newline="" para evitar líneas en blanco
    # y encoding="utf-8" para que soporte caracteres especiales
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        # Creo un objeto DictWriter para escribir diccionarios en CSV con los encabezados especificados
        writer = csv.DictWriter(f, fieldnames=["nombre", "precio", "cantidad"])
        writer.writeheader()  # Escribo la fila de encabezado
        writer.writerows(lista_inventario)  # Escribo todas las filas del inventario
    # Muestro un mensaje indicando que se guardó correctamente
    print(f"Inventario guardado en {archivo}")


# -------------------- FUNCION PARA CARGAR INVENTARIO --------------------
def cargar_inventario(lista_inventario, archivo="HV_week_3-main\inventario.csv", opcion="sobrescribir"):
    nueva_lista = []  # Creo una lista temporal para almacenar los productos leídos
    filas_invalidas = 0  # Contador de filas que no se pudieron procesar

    try:
        # Intento abrir el archivo en modo lectura
        with open(archivo, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)  # Uso DictReader para leer filas como diccionarios
            for fila in reader:
                try:
                    # Valido que la fila tenga las claves correctas y los tipos correctos
                    nombre = fila["nombre"]
                    precio = float(fila["precio"])  # Convierto precio a float
                    cantidad = int(fila["cantidad"])  # Convierto cantidad a int
                    # Si todo está bien, agrego el producto a la lista temporal
                    nueva_lista.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
                except (ValueError, KeyError):
                    # Si hay un error en los datos, aumento el contador de filas inválidas
                    filas_invalidas += 1

        # Ahora decido qué hacer según la opción indicada
        if opcion == "sobrescribir":
            lista_inventario.clear()  # Borro la lista actual
            lista_inventario.extend(nueva_lista)  # La reemplazo con los datos del CSV
        elif opcion == "fusionar":
            lista_inventario.extend(nueva_lista)  # Agrego los datos del CSV al inventario existente
        else:
            # Si la opción es inválida, uso sobrescribir por defecto
            print("Opción inválida, usando sobrescribir por defecto.")
            lista_inventario.clear()
            lista_inventario.extend(nueva_lista)

        # Muestro un mensaje indicando cuántas filas se cargaron y cuántas fueron inválidas
        print(f"Inventario cargado desde {archivo}. Filas inválidas: {filas_invalidas}")

    except FileNotFoundError:
        # Si el archivo no existe, informo al usuario
        print(f"Archivo {archivo} no encontrado.")
