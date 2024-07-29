class local:
    @staticmethod
    def login():


        if usuario.get()=="admin" and contrasena.get()== "admin":
            messagebox.showinfo(message="Bienvenido al sistema")
            local.menuPrincipal()
        else:
            messagebox.showerror(message="Usuario y/o contraseña incorrectos")
    @staticmethod
    def menuPrincipal():
        loginFrame.pack_forget()

        menuBarra = tk.Menu(root)

        almacen_menu = tk.Menu(menuBarra, tearoff=0)
        almacen_menu.add_command(label="Añadir", command=local.añadirProcuto)
        almacen_menu.add_command(label="Modificar", command=local.modificarProducto)
        #almacen_menu.add_command(label="Eliminar", command=almacen_eliminar)
        menuBarra.add_cascade(label="Almacén", menu=almacen_menu)

        # Menú Venta
        venta_menu = tk.Menu(menuBarra, tearoff=0)
        #venta_menu.add_command(label="Añadir", command=venta_añadir)
        #venta_menu.add_command(label="Modificar", command=venta_modificar)
        #venta_menu.add_command(label="Eliminar", command=venta_eliminar)
        menuBarra.add_cascade(label="Venta", menu=venta_menu)

        # Menú Compra
        compra_menu = tk.Menu(menuBarra, tearoff=0)
        #compra_menu.add_command(label="Añadir", command=compra_añadir)
        #compra_menu.add_command(label="Modificar", command=compra_modificar)
        #compra_menu.add_command(label="Eliminar", command=compra_eliminar)
        menuBarra.add_cascade(label="Compra", menu=compra_menu)

        # Configurar el menú
        root.config(menu=menuBarra)


    def añadirProcuto(self):
            local.ocultarFrame()


            id= idProducto
            id = int(id)+1
            nombre = nombreProducto.get()
            precio = int(precioProducto.get())
            cantidad = cantidadProducto.get()
            objProducto = articulo(id,nombre,precio,cantidad)
            listaProductos=[]
            listaProductos.append(objProducto)

            for i in listaProductos:
                print(i)

            anadirProductoFrame.pack()

    @staticmethod
    def modificarProducto():
        local.ocultarFrame()
        local.limpiarFrame(modificarProductoFrame)


        tk.Label(modificarProductoFrame, text="Ingrese ID del Producto").pack()
        producto = tk.Entry(modificarProductoFrame)
        producto.pack()

        modificarProductoFrame.pack()

    @staticmethod
    def ocultarFrame():
        for frame in frames:
            frame.pack_forget()

    @staticmethod
    def limpiarFrame(frame):
        for widget in frame.winfo_children():
            widget.destroy()






