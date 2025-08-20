#inventario = {
#    "manzanas": 10,
#    "naranjas": 5,
 #   "platanos": 8,
 #   "uvas": 15

#}
#print("Inventario inicial:", inventario)
# Agregar un nuevo producto
#inventario["peras"] = 12
#print("Inventario después de agregar peras:", inventario)
# vender  cualquier producto
#producto_vendido = "naranjas"
#cantidad_vendida = 3
#if producto_vendido in inventario:
#    if inventario[producto_vendido] >= cantidad_vendida:
#        inventario[producto_vendido] -= cantidad_vendida
#        print(f"Se vendieron {cantidad_vendida} {producto_vendido}.")
 #   else:
#        print(f"No hay suficiente {producto_vendido} en inventario.")
#else:
 #   print(f"{producto_vendido} no está en el inventario.")
#print("Inventario después de la venta:", inventario)

inventario = {}

print("Bienvenido al programa")
while True:
    print("1. Agregar productos")
    print("2. Vender productos")
    print("3. Mostrar inventario")
    print("0. Salir")

    opcion = int(input())

    if opcion == 1:
        nombre_producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))

        if nombre_producto in inventario:
            inventario[nombre_producto] += cantidad
        else:
            inventario[nombre_producto] = cantidad

        print("Inventario actualizado!")

    elif opcion == 2:
        producto = input("Ingrese el nombre del producto a vender: ")

        if nombre_producto in inventario:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if inventario[nombre_producto] >= cantidad:
                inventario[nombre_producto] -= cantidad
                print("Inventario actualizado!")
            else:
                print("No hay cantidad del producto")
        else:
            print("El producto no existe")
    elif opcion == 3:
        print(inventario)
    elif opcion == 0:
        print("Hasta luego")
        break
    else:
        print("Opción no válida")