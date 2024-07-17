import copy
class venta:

    def agregarVenta(self,id,fechaVenta,importeTotal,importeNeto,metodoPago):
        self.id = id
        self.fechaVenta = fechaVenta
        self.importeTotal = importeTotal
        self.importeNeto = importeNeto
        self.metodoPago = metodoPago

    def ventaProductos(self,listaProductos):
        i = ""
        listaProductosRetorno = []
        copiaLista = copy.deepcopy(listaProductos)
        while i!="2":
            print("Que producto decea agregar")
            for product in listaProductos:
                print(product.id,product.nombre,product.precio,product.cantidad)

            idProducto = int(input("Ingrese id Producto "))
            idProducto = idProducto-1
            cantidadProducto = int(input("Ingrese cantidad Producto que decea"))


            listaProductos[idProducto].cantidad  = listaProductos[idProducto].cantidad - cantidadProducto


            copiaLista[idProducto].cantidad = cantidadProducto

            listaProductosRetorno.append(copiaLista[idProducto])
            i = input("¿Desea Agregar otro producto?\n"
                  "1.- si\n"
                  "2.- no\n")
        return listaProductosRetorno

    def importe(self,listaVentaProductos):
        importeTotal = 0.0

        for product in listaVentaProductos:
            importeTotal = importeTotal+product.precio*product.cantidad

        return importeTotal