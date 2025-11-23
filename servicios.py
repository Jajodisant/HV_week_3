# -------------------- FUNCION PARA MOSTRAR PRODUCTOS --------------------
def mostrar_productos(lista_inventario: list):
    # Primero verifico si la lista está vacía
    if not lista_inventario:
        print("Inventario vacío.")  # Aviso que no hay productos
        return  # Salgo de la función

    i = 0  # Creo un contador para numerar los productos

    # Recorro cada producto en la lista de inventario
    for producto in lista_inventario:
        # Muestro el número del producto y su información
        print(f"Producto #{i + 1} = {producto}")
        i += 1  # Aumento el contador


# -------------------- FUNCION PARA AGREGAR PRODUCTO --------------------
def agregar_producto(lista_inventario: list, producto: dict):
    # Agrego el producto al final de la lista
    lista_inventario.append(producto)
    # Retorno la lista actualizada (aunque no es estrictamente necesario)
    return lista_inventario


# -------------------- FUNCION PARA ACTUALIZAR PRODUCTO --------------------
def actualizar_producto(lista_inventario: list, nombre: str, nuevo_precio: float=None, nueva_cantidad: int=None):
    # Recorro cada producto buscando por el nombre
    for producto in lista_inventario:
        if nombre != producto["nombre"]:
            continue  # Si el nombre no coincide, sigo con el siguiente producto
        else:
            # Si el nombre coincide, actualizo la cantidad y el precio
            producto["cantidad"] = nueva_cantidad
            producto["precio"] = nuevo_precio
            return producto  # Retorno el producto actualizado


# -------------------- FUNCION PARA ELIMINAR PRODUCTO --------------------
def eliminar_producto(lista_inventario: list, nombre: str):
    # Recorro cada producto buscando por nombre
    for producto in lista_inventario:
        if nombre != producto["nombre"]:
            continue  # Si no coincide, sigo con el siguiente
        else:
            # Si coincide, elimino el producto de la lista
            lista_inventario.remove(producto)
            return lista_inventario  # Retorno la lista actualizada


# -------------------- FUNCION PARA BUSCAR PRODUCTO --------------------
def buscar_producto(lista_inventario: list, nombre: str):
    # Recorro la lista buscando un producto por nombre
    for producto in lista_inventario:
        if nombre != producto["nombre"]:
            continue  # Si no coincide, sigo buscando
        else:
            return producto  # Retorno el producto encontrado


# -------------------- FUNCION PARA CALCULAR ESTADISTICAS --------------------
def calcular_estadisticas(lista_inventario):
    # Inicializo las variables que voy a usar para las estadísticas
    totalProductosRegistrados = 0
    valorTotalInventario = 0.0
    precio_mayor = 0.0
    mayor_stock = 0

    # Verifico si la lista está vacía
    if not lista_inventario:
        print("Inventario vacío.")  # Aviso al usuario
        return  # Salgo de la función

    # Recorro cada producto para calcular estadísticas
    for producto in lista_inventario:
        totalProductosRegistrados += producto["cantidad"]  # Sumo las cantidades
        valorTotalInventario += (producto["precio"] * producto["cantidad"])  # Sumo el valor total
        if precio_mayor < producto["precio"]:
            precio_mayor = producto["precio"]  # Guardo el precio más alto
        if mayor_stock < producto["cantidad"]:
            mayor_stock = producto["cantidad"]  # Guardo la cantidad más alta

    # Retorno un resumen con todas las estadísticas calculadas
    return (f"      Valor total del inventario: ${valorTotalInventario}\n\
                Cantidad total de productos registrados: {totalProductosRegistrados}\n\
                Producto mas caro: {precio_mayor}\n\
                Producto con mayor stock: {mayor_stock}")
