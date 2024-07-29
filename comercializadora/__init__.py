import copy
import tkinter as tk
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from productos import articulo
from venta import venta
from cliente import Cliente
from functools import partial
from datetime import datetime
import uuid
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import webbrowser
from tkinter import Toplevel, Label
import random
from tkinter import ttk
# Generar un UUID


listaProductos = [
    articulo(1, "dogChauw", 350, 50),
    articulo(2, "dogBite", 300, 40),
    articulo(3, "puppyLove", 250, 60),
    articulo(4, "dogFeast", 400, 30),
    articulo(5, "dogDelight", 280, 45)
]
listaVenta = []
listaFacturas = []
listaClientes=[
    Cliente(1, "Carlos", "García", "López", "555-1234", "Calle Falsa 123, Ciudad", "carlos.garcia@example.com"),
    Cliente(2, "María", "Pérez", "Hernández", "555-5678", "Avenida Siempre Viva 456, Ciudad", "maria.perez@example.com"),
    Cliente(3, "Juan", "Martínez", "Gómez", "555-8765", "Boulevard Principal 789, Ciudad", "juan.martinez@example.com"),
    Cliente(4, "Ana", "Sánchez", "Rodríguez", "555-4321", "Calle Secundaria 101, Ciudad", "ana.sanchez@example.com"),
    Cliente(5, "Luis", "Hernández", "Fernández", "555-2345", "Avenida Tercera 202, Ciudad", "luis.hernandez@example.com"),
    Cliente(6, "Laura", "Ruiz", "Díaz", "555-3456", "Calle Cuarta 303, Ciudad", "laura.ruiz@example.com"),
    Cliente(7, "Pedro", "Jiménez", "Morales", "555-4567", "Avenida Quinta 404, Ciudad", "pedro.jimenez@example.com"),
    Cliente(8, "Sofía", "Romero", "García", "555-5679", "Boulevard Secundario 505, Ciudad", "sofia.romero@example.com"),
    Cliente(9, "Miguel", "Torres", "Ramírez", "555-6789", "Calle Quinta 606, Ciudad", "miguel.torres@example.com"),
    Cliente(10, "Lucía", "Vargas", "Méndez", "555-7890", "Avenida Sexta 707, Ciudad", "lucia.vargas@example.com")
]

def login():
        if usuario.get()=="admin" and contrasena.get()== "admin":
            messagebox.showinfo(message="Bienvenido al sistema")
            menuPrincipal()
        else:
            messagebox.showerror(message="Usuario y/o contraseña incorrectos")

def menuPrincipal():
        loginFrame.pack_forget()

        menuBarra = tk.Menu(root)

        almacen_menu = tk.Menu(menuBarra, tearoff=0)
        almacen_menu.add_command(label="Añadir",command=añadirProducto)
        almacen_menu.add_command(label="Modificar", command=modificarProducto)
        almacen_menu.add_command(label="Eliminar", command=eliminarProducto)
        almacen_menu.add_command(label="Mostrar Productos",command=mostrarProductos)
        almacen_menu.add_command(label="Stock Bajo", command=stockBajo)
        menuBarra.add_cascade(label="Almacén", menu=almacen_menu)


        venta_menu = tk.Menu(menuBarra, tearoff=0)
        venta_menu.add_command(label="Añadir Venta", command=ventaProductos)
        venta_menu.add_command(label="ticket", command=ticketVenta)
        venta_menu.add_command(label="Historial de Ventas", command=mostrarVentas)
        menuBarra.add_cascade(label="Venta", menu=venta_menu)


        cliente_menu = tk.Menu(menuBarra, tearoff=0)
        cliente_menu.add_command(label="Registrar Cliente", command=registrarCliente)
        cliente_menu.add_command(label="Mostrar Clientes", command=mostrarClientes)
        cliente_menu.add_command(label="Modificar Cliente", command=modificarCliente)
        menuBarra.add_cascade(label="Cliente", menu=cliente_menu)

        reportesMenu = tk.Menu(menuBarra,tearoff=0)
        reportesMenu.add_command(label="Generar Reportes",command=reporteVenta)

        menuBarra.add_cascade(label="Reportes", menu=reportesMenu)

        # Configurar el menú
        root.config(menu=menuBarra)
def mostrarProductos():
    ocultarFrame()
    limpiarFrame(mostrarProductosFrame)

    global tree
    tree = ttk.Treeview(mostrarProductosFrame, columns=("ID", "Nombre", "Precio", "Cantidad"), show="headings")

    # Configurar las columnas
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Precio", text="Precio")
    tree.heading("Cantidad", text="Cantidad")

    tree.column("ID", width=50)
    tree.column("Nombre", width=150)
    tree.column("Precio", width=100)
    tree.column("Cantidad", width=100)

    tree.pack(fill=tk.BOTH, expand=True)

    for item in tree.get_children():
        tree.delete(item)
    # Agregar productos al Treeview
    for producto in listaProductos:
        tree.insert("", "end", values=(producto.id, producto.nombre, producto.precio, producto.cantidad))


    mostrarProductosFrame.pack()

def mostrarVentas():
    ocultarFrame()
    limpiarFrame(reporteVentasFrame)

    tree = ttk.Treeview(reporteVentasFrame, columns=("ID Venta", "Fecha Venta", "Carrito", "Importe Total","Importe Neto","Metodo Pago"), show="headings",height=100)

    # Configurar las columnas
    tree.heading("ID Venta", text="ID Venta")
    tree.heading("Fecha Venta", text="Fecha Venta")
    tree.heading("Carrito", text="Carrito")
    tree.heading("Importe Total", text="Importe Total")
    tree.heading("Importe Neto", text="Importe Neto")
    tree.heading("Metodo Pago", text="Metodo Pago")

    tree.column("ID Venta", width=70)
    tree.column("Fecha Venta", width=150)
    tree.column("Carrito", width=150)
    tree.column("Importe Total", width=100)
    tree.column("Importe Neto", width=100)
    tree.column("Metodo Pago", width=100)

    tree.pack(fill=tk.BOTH, expand=True)


    for vent in listaVenta:
       tree.insert("", "end", values=(vent.id,vent.fechaVenta,vent.carritoComprasLista,vent.importeTotal,vent.importeNeto,vent.metodoPago))



    reporteVentasFrame.pack()

def mostrarClientes():
    ocultarFrame()
    limpiarFrame(mostrarClientesFrame)
    tree = ttk.Treeview(mostrarClientesFrame, columns=("ID Cliente", "Nombre", "Apellido Paterno", "Apellido Materno","Telefono","Direccion","Correo"), show="headings")

    # Configurar las columnas
    tree.heading("ID Cliente", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Apellido Paterno", text="Apellido Paterno")
    tree.heading("Apellido Materno", text="Apellido Materno")
    tree.heading("Telefono", text="Telefono")
    tree.heading("Direccion", text="Direccion")
    tree.heading("Correo", text="Correo")


    tree.column("ID Cliente", width=50)
    tree.column("Nombre", width=100)
    tree.column("Apellido Paterno", width=100)
    tree.column("Apellido Materno", width=100)
    tree.column("Telefono", width=120)
    tree.column("Direccion", width=200)
    tree.column("Correo", width=200)

    tree.pack(fill=tk.BOTH, expand=True)

    # Agregar productos al Treeview
    for item in tree.get_children():
        tree.delete(item)
    for client in listaClientes:
        tree.insert("", "end", values=(client.id, client.nombre, client.apellidoPaterno, client.apellidoMaterno, client.telefono, client.direccion, client.correo))


    mostrarClientesFrame.pack()
def actualizarProductos(lista):
    for item in tree.get_children():
        tree.delete(item)
    for producto in lista:
        tree.insert("", "end", values=(producto.id, producto.nombre, producto.precio, producto.cantidad))
def añadirProducto():

            def a():
                try:
                    v = int(cantidadProducto.get())
                    v2 = int(precioProducto.get())
                except ValueError:
                    messagebox.showerror(message="Error al agregar, Campos Vacios")
                try:
                    if v >=0 and v2>0:
                        try:
                            nombre = nombreProducto.get()
                            precio= int(precioProducto.get())
                            cantidad = int(cantidadProducto.get())
                            ideProducto = random.randint(6,9999)
                            limpiarCampos(anadirProductoFrame)
                            objProducto = articulo(ideProducto,nombre,precio,cantidad)
                            listaProductos.append(objProducto)

                            articulo.mostrarProducto(listaProductos)
                            messagebox.showinfo(message="Producto Agregado Correctamente")
                        except ValueError:
                            messagebox.showerror(message="Error al Agregar, Campo Vacio")
                    else:
                        messagebox.showerror(message="Cantidad y/o Precio incalidos")
                except UnboundLocalError:
                    messagebox.showerror(message="no se agrego Producto")




            ocultarFrame()
            limpiarFrame(anadirProductoFrame)
            tk.Label(anadirProductoFrame, text="Nombre del Producto").pack()
            nombreProducto = tk.Entry(anadirProductoFrame)
            nombreProducto.pack()

            tk.Label(anadirProductoFrame, text="Precio Producto").pack()
            precioProducto = tk.Entry(anadirProductoFrame)
            precioProducto.pack()

            tk.Label(anadirProductoFrame, text="Cantidad").pack()
            cantidadProducto = tk.Entry(anadirProductoFrame)
            cantidadProducto.pack()

            tk.Button(anadirProductoFrame, text="Añadir Producto", command=a).pack()



            anadirProductoFrame.pack()

def modificarProducto():

        ocultarFrame()
        limpiarFrame(modificarProductoFrame)


        mostrarProductos()
        tk.Label(modificarProductoFrame, text="Ingrese ID del Producto").pack()
        idProducto = tk.Entry(modificarProductoFrame)
        idProducto.pack()

        def llamadoModificar():
            try:
                identificador = None
                ide = int(idProducto.get())
                for i in listaProductos:
                    if i.id == ide:
                        limpiarFrame(modificarProductoFrame)
                        articulo.modificarProducto(modificarProductoFrame, listaProductos, ide)




            except ValueError:
                messagebox.showerror(message="Error al Modificar, Id Invalido")

        tk.Button(modificarProductoFrame,text="Modificar",command = llamadoModificar).pack()
        #partial(articulo.modificarProducto, atributos
        modificarProductoFrame.pack()

def eliminarProducto():
    ocultarFrame()
    limpiarFrame(eliminarProductoFrame)

    mostrarProductos()

    tk.Label(eliminarProductoFrame, text="Ingrese ID del Producto").grid()
    idProducto = tk.Entry(eliminarProductoFrame)
    idProducto.grid()
    try:
        def llamarEliminar():
            try:
                id = int(idProducto.get())
                articulo.eliminarProducto(root,eliminarProductoFrame,listaProductos,id)
                actualizarProductos(listaProductos)
                eliminarProducto()
            except ValueError:
                messagebox.showerror(message="Error al Eliminar, Id Invalido")
    except ValueError:
        messagebox.showerror(message="Error al Eliminar, Id Invalido")

    tk.Button(eliminarProductoFrame, text="Eliminar",command=llamarEliminar).grid()
    eliminarProductoFrame.pack()

def stockBajo():
    ocultarFrame()
    limpiarFrame(mostrarProductosFrame)

    headers = ["ID", "Nombre", "Precio", "Cantidad"]
    header_str = "{:<10} {:<30} {:<20} {:<10}".format(*headers)
    tk.Label(mostrarProductosFrame, text=header_str, font=("Arial", 8, "bold")).grid(row=0, column=0, padx=5,
                                                                                     pady=5)

    listbox = tk.Listbox(mostrarProductosFrame, height=10, width=50)

    for producto in listaProductos:
        if producto.cantidad < 5:
            item_str = "{:<10} {:<30} {:<20} {:<30}".format(
                producto.id, producto.nombre, producto.precio, producto.cantidad
            )
            listbox.insert(tk.END, item_str)

    listbox.grid(row=1, column=0, padx=5, pady=5)

    mostrarProductosFrame.pack()


def ventaProductos():

    ocultarFrame()
    limpiarFrame(anadirVentaFrame)
    mostrarProductos()
    ventaProd = venta()

    carrito = ventaProd.agregarCarrito(listaProductos,anadirVentaFrame,root)

    def final():
            if carrito == "":
                messagebox.showerror(message="Carrito Vacio, no se agrego la compra")
                ventaProductos()
            else:
                pago = combobx.get()
                carritoCopia = copy.deepcopy(carrito)
                importe = 0.0
                importe = ventaProd.importe(carritoCopia)
                indice = 0
                fecha = datetime.now()
                global ventaReciente
                ideProducto = random.randint(10,9999)

                print(pago)
                ventaReciente= venta(ideProducto, fecha,carritoCopia, importe, importe * 1.16, pago)
                indice +=1
                listaVenta.append(ventaReciente)


                carrito.clear()
                actualizarProductos(listaProductos)
                messagebox.showinfo(message="Venta Finalizada")

    pago = ["Tarjeta", "Efectivo"]
    combobx = ttk.Combobox(anadirVentaFrame, values=pago)
    combobx.set("Metodo de Pago")
    combobx.pack()
    tk.Button(anadirVentaFrame, text="Terminar Compra", command=final).pack()

    anadirVentaFrame.pack()

def ticketVenta():
    ocultarFrame()
    limpiarFrame(ticketVentaFrame)

    def pdfTicket(filename, obj):
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter

        # Añadir título
        c.setFont("Helvetica-Bold", 24)
        c.drawString(100, height - 50, "Ticket")


        c.setFont("Helvetica", 12)
        y_position = height - 100
        venta_str = str(obj)
        for line in venta_str.split("\n"):
            c.drawString(100, y_position, line)
            y_position -= 20

        # Finalizar y guardar el PDF
        c.showPage()
        c.save()
    def generarTicket():
        try:
            nombre = "Ticket.pdf"
            pdfTicket(nombre, ventaReciente)
            messagebox.showinfo(message="Ticket Generado")
        except NameError:
            messagebox.showerror(message="No hay Venta para generar Ticket")

        try:
            webbrowser.open_new("C:\\Users\\israe\\PycharmProjects\\comercializadoraConsola\\Ticket.pdf")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el PDF en el navegador: {e}")

    ticket = tk.Button(ticketVentaFrame,text="Generar Ticket",command=generarTicket)
    ticket.pack(expand=True, fill='both')


    def factu():
        ocultarFrame()
        limpiarFrame(generarFacturaFrame)
        mostrarClientes()

        def pdfFactura(filename, objTik, objFactura):
            c = canvas.Canvas(filename, pagesize=letter)
            width, height = letter

            # Añadir título
            c.setFont("Helvetica-Bold", 24)
            c.drawString(100, height - 50, "Factura")

            c.setFont("Helvetica", 12)
            y_position = height - 100
            cliente_str = str(objFactura)
            for line in cliente_str.split("\n"):
                c.drawString(100, y_position, line)
                y_position -= 20

            venta_str = str(objTik)
            for line in venta_str.split("\n"):
                c.drawString(100, y_position, line)
                y_position -= 20

            # Finalizar y guardar el PDF
            c.showPage()
            c.save()

        def generarFactura():
            idC = int(idCnt.get())

            infoFactura = listaClientes[idC-1]
            listaFacturas.append(infoFactura)

            nombre = "Factura.pdf"
            ventaReci = listaVenta[len(listaVenta)-1]
            pdfFactura(nombre,ventaReci, infoFactura)
            messagebox.showinfo(message="Factura Generada")
            try:
                webbrowser.open_new("C:\\Users\\israe\\PycharmProjects\\comercializadoraConsola\\Factura.pdf")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el PDF en el navegador: {e}")

        tk.Label(generarFacturaFrame,text="id CLiente").pack()
        idCnt = tk.Entry(generarFacturaFrame)
        idCnt.pack()

        tk.Button(generarFacturaFrame,text="Generar Factura",command=generarFactura).pack()
        tk.Frame(ticketVentaFrame).pack()

        generarFacturaFrame.pack()
    fatura = tk.Button(ticketVentaFrame,text="Factura",command=factu)
    fatura.pack(expand=True, fill='both')

    ticketVentaFrame.pack(fill=tk.BOTH, expand=True)

def reporteVenta():
    ocultarFrame()
    limpiarFrame(reporteVentasFrame)

    productosMasVendidos = {}
    listanomProducto = []
    def generarListaSalidas():

        for vendido in listaVenta:
            for carrito in vendido.carritoComprasLista:
                if carrito.id in productosMasVendidos:
                    productosMasVendidos[carrito.id].precio += carrito.precio * carrito.cantidad
                    productosMasVendidos[carrito.id].cantidad += carrito.cantidad
                else:

                    carritoCopia = copy.deepcopy(carrito)
                    carritoCopia.precio *= carritoCopia.cantidad
                    productosMasVendidos[carrito.id] = carritoCopia


    def masVendido():
        generarListaSalidas()

        listaMasVendido = list(productosMasVendidos.values())
        limpiarFrame(reporteVentasFrame)
        tk.Button(reporteVentasFrame, text="Regresar", command=reporteVentasFrame)
        venta.reporteMasVendido(listaMasVendido,reporteVentasFrame)

        for i in listaMasVendido:
            print(i.nombre, i.cantidad)
        listaMasVendido.clear()
    def ventaDia():


        print()
    def masIngresos():
        generarListaSalidas()

        listaMasVendido = list(productosMasVendidos.values())
        limpiarFrame(reporteVentasFrame)
        tk.Button(reporteVentasFrame, text="Regresar", command=reporteVentasFrame)
        venta.masIngresos(listaMasVendido, reporteVentasFrame)
        for i in listaMasVendido:
            print(i.nombre, i.precio)
        listaMasVendido.clear()
        print()
    try:
        boton1 = tk.Button(reporteVentasFrame,text="Reporte Producto mas Vendido",command=masVendido)
        boton1.pack(fill=tk.BOTH, expand=True)
        #tk.Button(reporteVentasFrame,text="Reporte Ventas por dia").pack()

        boton2 = tk.Button(reporteVentasFrame,text="Ingresos por Producto",command=masIngresos)
        boton2.pack(fill=tk.BOTH, expand=True)
    except(ValueError, TypeError):
        messagebox.showerror(message="No hay Venta")
    reporteVentasFrame.pack(fill=tk.BOTH, expand=True)

def registrarCliente():
    ocultarFrame()
    limpiarFrame(añadirClienteFrame)

    def aggCliente():
        if nombre.get() == "" or apPaterno.get() == "" or apMaterno.get() == "":
            messagebox.showerror(message="Error al Agregar, Campos vacios o invalidos")
        else:
            nom = nombre.get()
            paterno = apPaterno.get()
            materno = apMaterno.get()
            cel = tel.get()
            direc = direccion.get()
            corr = correo.get()
            limpiarCampos(añadirClienteFrame)
            ideCliente = random.randint(10,9999)
            objCliente = Cliente(ideCliente,nom,paterno,materno,cel,direc,corr)
            #nuevoCliente = objCliente.agregarCliente(1,nom,paterno,materno,cel,direc,corr)
            listaClientes.append(objCliente)
            print(listaClientes)
            messagebox.showinfo(message="CLiente Agregado")

    tk.Label(añadirClienteFrame,text="Nombre").pack()
    nombre = tk.Entry(añadirClienteFrame)
    nombre.pack()

    tk.Label(añadirClienteFrame,text="Apellido Paterno").pack()
    apPaterno = tk.Entry(añadirClienteFrame)
    apPaterno.pack()

    tk.Label(añadirClienteFrame,text="Apellido Materno").pack()
    apMaterno = tk.Entry(añadirClienteFrame)
    apMaterno.pack()

    tk.Label(añadirClienteFrame,text="Telefono").pack()
    tel = tk.Entry(añadirClienteFrame)
    tel.pack()

    tk.Label(añadirClienteFrame,text="Direccion").pack()
    direccion = tk.Entry(añadirClienteFrame)
    direccion.pack()

    tk.Label(añadirClienteFrame,text="Correo Electronico").pack()
    correo = tk.Entry(añadirClienteFrame)
    correo.pack()


    tk.Button(añadirClienteFrame,text="Agregar Cliente",command=aggCliente).pack()

    añadirClienteFrame.pack()

def modificarCliente():
    ocultarFrame()
    limpiarFrame(modificarClienteFrame)

    mostrarClientes()

    def modificarC():
        try:
            idCte = int(idCnte.get())
            limpiarFrame(modificarClienteFrame)
            tk.Button(modificarClienteFrame, text="Regresar", command=modificarCliente).pack()
            objCliente = Cliente()
            objCliente.modificarCliente(idCte,listaClientes,modificarClienteFrame)
        except ValueError:
            messagebox.showerror(message="Ingrese ID valida")

    try:
        tk.Label(modificarClienteFrame,text="Ingrese ID CLiente").pack()
        idCnte = tk.Entry(modificarClienteFrame)
        idCnte.pack()

        tk.Button(modificarClienteFrame,text="Aceptar",command=modificarC).pack()
    except ValueError:
        messagebox.showerror(message="ingrese ID correcta")
    modificarClienteFrame.pack(fill=tk.BOTH, expand=True)

def ocultarFrame():
        for frame in frames:
            frame.pack_forget()
def limpiarFrame(frame):
        for widget in frame.winfo_children():
            widget.destroy()

def limpiarCampos(frame):
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)


root = tk.Tk()

#dimensiones: ancho por altura
root.geometry("1000x600")

root.configure(background="white")
tk.Wm.wm_title(root,"Menu principal")
loginFrame = tk.Frame(root)
loginFrame.pack()


tk.Label(loginFrame,text="Usuario").pack()
usuario = tk.Entry(loginFrame)
usuario.pack()

tk.Label(loginFrame,text="Contraseña").pack()
contrasena = tk.Entry(loginFrame,show="*")
contrasena.pack()

tk.Button(loginFrame,text="Aceptar",command=login).pack()

#principalFrame = tk.Frame(root)


mostrarProductosFrame = tk.Frame(root)
anadirProductoFrame = tk.Frame(root)
modificarProductoFrame = tk.Frame(root)
eliminarProductoFrame = tk.Frame(root)
stockBajoFrame = tk.Frame(root)
anadirVentaFrame = tk.Frame(root)
ticketVentaFrame = tk.Frame(root)
reporteVentasFrame = tk.Frame(root)
generarFacturaFrame = tk.Frame(root)
mostrarClientesFrame = tk.Frame(root)
añadirClienteFrame = tk.Frame(root)
modificarClienteFrame = tk.Frame(root)
eliminarClienteFrame = tk.Frame(root)
añadirProvedorFrame = tk.Frame(root)
modificarProvedorFrame = tk.Frame(root)
eliminarProvedprFrame = tk.Frame(root)
mostrarProvedoresFrame = tk.Frame(root)




frames = [
    mostrarProductosFrame,anadirProductoFrame,modificarProductoFrame,eliminarProductoFrame,stockBajoFrame,
    anadirVentaFrame,ticketVentaFrame,reporteVentasFrame,generarFacturaFrame,
    mostrarClientesFrame,añadirClienteFrame,modificarClienteFrame,eliminarClienteFrame,añadirProvedorFrame
    ,modificarProvedorFrame,eliminarProvedprFrame,mostrarProvedoresFrame
]



tk.mainloop()

