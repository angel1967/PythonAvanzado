# Reto 1 Inventario de productos
# Alumno: Miguel Angel Castañeda

import datetime

# Clase para representar un producto en el Inventario
class Product:
    def __init__(self, name, quantity, price, type, size):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.type = type
        self.size = size

# Lista para guardar los productos del Inventario
inventory = []

# Funcion para añadir un producto en el inventario
def add_product():
    name = input("Enter the product name: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price: "))
    type = input("Enter the type: ")
    size = input("Enter the size: ")
    product = Product(name, quantity, price, type, size)
    inventory.append(product)
    print("Product added successfully.")

# Funcion para actualizar la cantidad de un producto en el inventario
def update_quantity():
    name = input("Enter the name of the product to update: ")
    new_quantity = int(input("Enter the new quantity: "))
    for product in inventory:
        if product.name == name:
            product.quantity = new_quantity
            print("Quantity updated successfully.")
            return
    print("The product is not found in the inventory.")

# Funcion de busqueda de un producto en el inventario
def search_product():
    name = input("Enter the name of the product to search: ")
    for product in inventory:
        if product.name == name:
            print("Name: ", product.name)
            print("Quantity: ", product.quantity)
            print("Price: ", product.price)
            print("Type: ", product.type)
            print("Size: ", product.size)
            return
    print("The product is not found in the inventory.")

# Funcion para sortear inventario por un atributo dado
def sort_inventory():
    option = input("Enter the attribute to sort the inventory by (name/quantity/price): ")
    
    if option == "name":
        inventory.sort(key=lambda x: x.name)
    elif option == "quantity":
        inventory.sort(key=lambda x: x.quantity)
    elif option == "price":
        inventory.sort(key=lambda x: x.price)
    else:
        print("Invalid option.")
        return
    
    print("Inventory sorted by", option, "successfully.")

# Funcion para generar un reporte de Inventario de productos
def generate_report():
    print("Inventory Report:")
    for product in inventory:
        print("Name: ", product.name)
        print("Quantity: ", product.quantity)
        print("Price: ", product.price)
        print("Type: ", product.type)
        print("Size: ", product.size)
        print("------------------------")

# Function para calcular el valor total del inventario
def calculate_total_value():
    total_value = 0
    for product in inventory:
        total_value += product.quantity * product.price
    print("The total value of the inventory is:", total_value)

# Funcion adicional 1: Calcula la cantidad total d eun tipo de producto
def calculate_total_quantity_by_type():
    type = input("Enter the type of product to calculate the total quantity: ")
    total_quantity = 0
    for product in inventory:
        if product.type == type:
            total_quantity += product.quantity
    print("The total quantity of", type, "products is:", total_quantity)

# Funcion adicional 2: Borra un producto del Inventario
def remove_product():
    name = input("Enter the name of the product to remove from the inventory: ")
    for product in inventory:
        if product.name == name:
            inventory.remove(product)
            print("Product removed successfully.")
            return
    print("The product is not found in the inventory.")

# Funcion adicional 3: Actualiza el precio del producto
def update_price():
    name = input("Enter the name of the product to update the price: ")
    new_price = float(input("Enter the new price: "))
    for product in inventory:
        if product.name == name:
            product.price = new_price
            print("Price updated successfully.")
            return
    print("The product is not found in the inventory.")

# Funcion principal del programa
def main():
    while True:
        print("==== Inventory System ====")
        print("1. Add product")
        print("2. Update quantity")
        print("3. Search product")
        print("4. Sort inventory")
        print("5. Generate inventory report")
        print("6. Calculate total inventory value")
        print("7. Calculate total quantity by type")
        print("8. Remove product")
        print("9. Update product price")
        print("10. Exit")
        
        option = int(input("Enter an option: "))
        
        if option == 1:
            add_product()
        elif option == 2:
            update_quantity()
        elif option == 3:
            search_product()
        elif option == 4:
            sort_inventory()
        elif option == 5:
            generate_report()
        elif option == 6:
            calculate_total_value()
        elif option == 7:
            calculate_total_quantity_by_type()
        elif option == 8:
            remove_product()
        elif option == 9:
            update_price()
        elif option == 10:
            break
        else:
            print("Invalid option.")

# Corre el programa principal
if __name__ == "__main__":
    main()
