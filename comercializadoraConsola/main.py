import tkinter
from productos import *
from venta import *

#inicio de sesion

idProducto=idProvedor=idCompra=idCliente=idVenta=1
listaProductos=listaProvedores=listaCompras=listaClientes=listaVentaProductos = []


while id != "s":
    log =""
    print("MENU")
    id = input("1.- Inventario \n"
               "2.- Venta de productos\n"
               "3.- Compra de productos\n"
               "s.- Salir\n")
    match id:
        case "1":
            caso1 = ""
            while caso1!="s":
                caso1=input("1.- Añadir producto\n"
                              "2.- Editar producto\n"
                              "3.- Eliminar producto\n"
                              "4.- ver Inventario\n"
                              "5.- Stock Bajo\n"
                              "s.- Menu Principal\n")
                match caso1:
                    case "1":
                        indice = 0

                        while indice != "2":
                            nombreProducto = input("ingrese el nombre del producto: ")
                            precioProducto = int(input("ingrse el precio del producto: "))
                            cantidadProducto = int(input("ingrese el cantidad de producto: "))

                            objProducto = articulo(idProducto, nombreProducto, precioProducto, cantidadProducto)

                            listaProductos.append(objProducto)
                            idProducto = idProducto + 1

                            indice = input("Desea Añadir otro Producto?\n"
                                           "1.-si\n"
                                           "2.-no\n")
                    case "2":
                        print("Lista de Articulos\n")
                        print(objProducto.mostrarProducto(listaProductos))

                        objProducto.modificarProducto(int(input("ingrese id del producto que decea modificar\n")), listaProductos)

                    case "3":
                        print(objProducto.mostrarProducto(listaProductos))
                        objProducto.eliminarProducto(int(input("ingrese id del producto que decea eliminar \n")),listaProductos)
                        print("producto eliminado\n")
                    case "4":
                        print(objProducto.mostrarProducto(listaProductos))

                    case "5":
                        objProducto.stockBajo(listaProductos)
                    case "s":
                        print("Menu Principal")

        case "2":
            caso2=input("1.- Registrar Nueva Venta\n"
                  "2.- Reporte de ventas\n"
                  "3.- Generar Factura (registro de cliente)\n"
                        "s.- Menu Principal\n")
            match caso2:
                case "1":
                    objVentas = venta()

                    listaVentaProductos = objVentas.ventaProductos(listaProductos)

                    for producto in listaVentaProductos:
                        print(producto.id,producto.nombre,producto.precio,producto.cantidad)

                    print()
                case "2":
                    print("Lista de Productos")
                    for product in listaVentaProductos:
                        print(product.id,product.nombre,product.precio,product.cantidad)

                    print("importe Total: $",objVentas.importe(listaVentaProductos) )
                    print("importe Neto : $",objVentas.importe(listaVentaProductos)*1.16 )
                case "3":
                    print()
                case "s":
                    print()
        case "3":
            caso3=input("1.- Lista Provedores\n"
                  "2.- Registrar Provedor\n"
                  "3.- Editar Provedor\n"
                  "4.- Eliminar Provedor\n"
                        "s.- Menu Principal\n")
            match caso1:
                case "1":
                    print()
                case "2":
                    print()
                case "3":
                    print()
                case "4":
                    print()
                case "s":
                    print()
        case "s":
            print("Adios\n")