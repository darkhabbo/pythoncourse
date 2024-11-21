#lista
inventario = [("Huevo de Parasaurolophus", 2, 5000), ("Huevo de Brachiosaurus", 5, 10000), ("Huevo de Tyrannosaurus rex", 2, 50000)]

# agregar producto:
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese Valor: "))
    # mostrar el producto en inventario
    inventario.append((nombre, cantidad, precio))
    print(f"Producto '{nombre}' Agregado con cantidad {cantidad} Precio: {precio}")

#mostrar los productos
def mostrar_productos():
    if inventario:
        print("\nLista de productos en el inventario:")
        for producto, cantidad, precio in inventario:
            print(f"Producto: {producto}, Cantidad: {cantidad}, Precio: {precio}")
    else:
        print("Lista vacía.")

# menu
def menu():
    while True:
        print("\n###__Menú Interactivo__###")
        print("1. Agregar productos")
        print("2. Mostrar productos")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            mostrar_productos()
        elif opcion == 3:
            print("Fin")
            break  
        else:
            print("3RR0R!!!!!!!!!!!!!")

#ejecutar el menu
menu()
