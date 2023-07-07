import datetime

# Clase para representar un artículo del inventario
class Producto:
    def __init__(self, nombre, cantidad, precio, tipo, tamaño):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.tipo = tipo
        self.tamaño = tamaño

# Función para agregar un nuevo artículo al inventario
def agregar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    tipo = input("Ingrese el tipo del producto: ")
    tamaño = input("Ingrese el tamaño del producto: ")
    producto = Producto(nombre, cantidad, precio, tipo, tamaño)
    inventario.append(producto)
    print("Producto agregado exitosamente.")

# Función para actualizar la cantidad de un artículo existente en el inventario
def actualizar_cantidad(inventario):
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la nueva cantidad del producto: "))
    for producto in inventario:
        if producto.nombre == nombre:
            producto.cantidad = cantidad
            print("Cantidad actualizada exitosamente.")
            return
    print("No se encontró el producto en el inventario.")

# Función para buscar un artículo específico en el inventario
def buscar_producto(inventario):
    criterio = input("Ingrese el criterio de búsqueda (nombre, tipo o tamaño): ")
    valor = input("Ingrese el valor a buscar: ")
    for producto in inventario:
        if criterio == "nombre" and producto.nombre == valor:
            mostrar_producto(producto)
            return
        elif criterio == "tipo" and producto.tipo == valor:
            mostrar_producto(producto)
            return
        elif criterio == "tamaño" and producto.tamaño == valor:
            mostrar_producto(producto)
            return
    print("No se encontró ningún producto que cumpla con el criterio de búsqueda.")

# Función auxiliar para mostrar los detalles de un artículo
def mostrar_producto(producto):
    print("Nombre: ", producto.nombre)
    print("Cantidad: ", producto.cantidad)
    print("Precio: ", producto.precio)
    print("Tipo: ", producto.tipo)
    print("Tamaño: ", producto.tamaño)

# Función para ordenar el inventario en función de diferentes atributos usando funciones lambda
def ordenar_inventario(inventario):
    opcion = input("Ingrese la opción de ordenamiento (nombre, cantidad o precio): ")
    if opcion == "nombre":
        inventario.sort(key=lambda x: x.nombre)
    elif opcion == "cantidad":
        inventario.sort(key=lambda x: x.cantidad)
    elif opcion == "precio":
        inventario.sort(key=lambda x: x.precio)
    else:
        print("Opción de ordenamiento inválida.")
        return
    print("Inventario ordenado exitosamente.")

# Función para generar un informe de inventario
def generar_informe(inventario):
    informe = ""
    for producto in inventario:
        informe += f"Nombre: {producto.nombre}\n"
        informe += f"Cantidad: {producto.cantidad}\n"
        informe += f"Precio: {producto.precio}\n"
        informe += f"Tipo: {producto.tipo}\n"
        informe += f"Tamaño: {producto.tamaño}\n"
        informe += "-" * 20 + "\n"
    return informe

# Función para calcular el valor total del inventario
def calcular_valor_total(inventario):
    valor_total = sum([producto.cantidad * producto.precio for producto in inventario])
    return valor_total

# Función para borrar un producto del inventario
def borrar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a borrar: ")
    for producto in inventario:
        if producto.nombre == nombre:
            inventario.remove(producto)
            print("Producto borrado exitosamente.")
            return
    print("No se encontró el producto en el inventario.")

# Función principal del programa
def main():
    inventario = []
    while True:
        print("\n---- Menú ----")
        print("1. Agregar producto")
        print("2. Actualizar cantidad de producto")
        print("3. Buscar producto")
        print("4. Ordenar inventario")
        print("5. Generar informe de inventario")
        print("6. Calcular valor total del inventario")
        print("7. Borrar producto del inventario")
        print("8. Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            agregar_producto(inventario)
        elif opcion == 2:
            actualizar_cantidad(inventario)
        elif opcion == 3:
            buscar_producto(inventario)
        elif opcion == 4:
            ordenar_inventario(inventario)
        elif opcion == 5:
            informe = generar_informe(inventario)
            print(informe)
        elif opcion == 6:
            valor_total = calcular_valor_total(inventario)
            print("El valor total del inventario es:", valor_total)
        elif opcion == 7:
            borrar_producto(inventario)
        elif opcion == 8:
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
