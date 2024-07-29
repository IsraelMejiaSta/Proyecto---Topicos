class provedores:

    def agregarProvedor(self,id, nombre,direccion,telefono,email,productos):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.productos = productos if productos is not None else []


    def __str__(self):
        carrito_str = "\n".join(str(producto) for producto in self.productos)
        return (
            f"Id provedor {self.id}\n"
            f"Nombre: {self.nombre}\n"
            f"Direccion: {self.direccion}\n"
            f"Telefono: {self.telefono}\n"
            f"Email: {self.email}\n"
            f"Productos: {carrito_str}"
        )

    def modificarProvedor(self,id,listaProvedor):
        id=id-1
        opcion = input("Que desea Modificar\n"
              "1.- Nombre\n"
              "2.- direccion\n"
              "3.- telefono\n"
              "4.- email\n"
                "s.- menu principal")

        match opcion:
            case "1":
                listaProvedor[id].nombre = input("Ingrese nuevo nombre")
            case "2":
                listaProvedor[id].direccion = input("Ingrese nueva direccion")
            case "3":
                listaProvedor[id].telefono = input("Ingrese nuevo telefono")
            case "4":
                listaProvedor[id].email = input("Ingrese email")
            case "s":
                ("Opcion Incorrecta")

    def eliminarProvedor(self,provedores,id):
        id-=1
        provedores.remove(provedores[id])
