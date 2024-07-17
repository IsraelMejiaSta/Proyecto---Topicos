class articulo:
    def __init__(self, id ,nombre,precio,cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad


    def mostrarProducto(self, listaProductos):
        for arti in listaProductos:
            print(arti.id,arti.nombre,arti.precio,arti.cantidad)


    def modificarProducto(self, id, listaProductos):
        id=id-1
        i = input("Modificar \n"
              "1.- Precio\n"
              "2.- Cantidad\n")
        if i == "1":
            listaProductos[id].precio = input("Ingrese Nuevo Precio")
        elif i == "2":
            cantidad = int(input("Ingrese Cantidad"))
            listaProductos[id].cantidad = listaProductos[id].cantidad+cantidad
        else:
            print("opcion incorrecta")

    def eliminarProducto(self,id,listaProductos):
        id=id-1
        listaProductos.remove(listaProductos[id])

    def stockBajo(self,listaProductos):
        for product in listaProductos:
            if product.cantidad <=5:
                print(product.id,product.nombre,product.precio,product.cantidad)


