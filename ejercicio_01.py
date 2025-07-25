def menu():
    print("\n--MENÚ--")
    print("1.Agregar un producto a la lista")
    print("2.Modificar un producto existente")
    print("3.Eliminar un producto")
    print("4.Ver todos los productos")
    print("5.Salir del programa")

while True:
    productos=[]
    menu()
    option=input("Seleccione una opción del menú (1-5): ")

    match option:
        case "1":
            p=input("Ingrese un producto a la lista: ")
            productos.append(p)
        case "2":
            print(f"La lista de sus productos es:{productos}")
            indice=int(input("Ingrese el numero de indice del producto que quiere remplazar:"))
            new_product=input("Ingrese el nuevo producto: ")
            productos[indice] = new_product
            print("Producto modificado.")

        case "3":

        case "4":

        case "5":
            print("Saliendo del programa")
            break
