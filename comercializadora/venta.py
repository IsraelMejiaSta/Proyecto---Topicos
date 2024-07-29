import copy
import tkinter as tk
import productos
from tkinter import messagebox
from productos import *
import matplotlib.pyplot as plt
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class venta:

    def __init__(self,id=0,fechaVenta="",carritoComprasLista=None,importeTotal=0.0,importeNeto=0.0,metodoPago=""):
        self.id = id
        self.fechaVenta = fechaVenta
        self.carritoComprasLista = carritoComprasLista if carritoComprasLista is not None else []
        self.importeTotal = importeTotal
        self.importeNeto = importeNeto
        self.metodoPago = metodoPago

    def __str__(self):
        carrito_str = "\n".join(str(producto) for producto in self.carritoComprasLista)
        return (f"ID de la Compra: {self.id}\n"
                f"Fecha: {self.fechaVenta}\n"
                f"Carrito de Compras:\n{carrito_str}\n"
                f"Importe Total: ${self.importeTotal:.2f}\n"
                f"Importe con IVA: ${self.importeNeto:.2f}\n"
                f"Método de Pago: {self.metodoPago}")

    @staticmethod
    def agregarCarrito(listaProductos,frame,root):

        listaCom = []

        def agregar():
            try:

                cNegativa = int(cd.get())
                id = int(idProducto.get())
                cant = int(cd.get())

                for widget in frame.winfo_children():
                    if isinstance(widget, tk.Entry):
                        widget.delete(0, tk.END)
                for obj in listaProductos:
                        if obj.id == id and (cNegativa > 0 and cNegativa<=obj.cantidad):

                                objeto = copy.deepcopy(obj)
                                objeto.cantidad = copy.deepcopy(cant)
                                listaCom.append(objeto)
                                listaProductos[id - 1].cantidad -= cant
                                contador =1
                                messagebox.showinfo(message="Producto Agregado")
                                break
                        else:
                            contador = 0

                if contador==0:
                    messagebox.showerror(message="id y/o cantidad no valida")



            except ValueError:
                messagebox.showerror(message="Campos Vacio o incorrectos")

        tk.Label(frame,text="Ingrese el id del producto").pack()
        idProducto = tk.Entry(frame)
        idProducto.pack()

        tk.Label(frame,text="Ingrese Cantidad del producto").pack()
        cd = tk.Entry(frame)
        cd.pack()

        tk.Button(frame,text="Agregar",command=agregar).pack()

        return listaCom

    @staticmethod
    def importe(lista):
        importeTot = 0.0

        for product in lista:
            importeTot = importeTot+ product.precio*product.cantidad

        return importeTot

    @staticmethod
    def reporteMasVendido (lista,root):
        nombres=[]
        cantidad=[]
        for producto in lista:
            nombres.append(producto.nombre)
            cantidad.append(int(producto.cantidad))

        figura,ax = plt.subplots()
        ax.set_title("Productos Mas Vendidos")
        ax.set_xlabel("Productos")
        ax.set_ylabel("Cantidad")
        ax.bar(nombres,cantidad)
        for i,txt in enumerate(cantidad):
            ax.annotate(txt,(i,cantidad[i]),textcoords="offset points",xytext=(0,10),ha="center")
        canvas = FigureCanvasTkAgg(figura, master = root)
        canvas.draw()

        canvas.get_tk_widget().pack()

        #ax.plot(nombres,cantidad,label='Productos',color='red',marker="x")
        #plt.show()

    @staticmethod
    def masIngresos(listaProductos,root):

        nombres=[]
        ingresos=[]

        for prodtucto in listaProductos:
            nombres.append(prodtucto.nombre)
            ingresos.append(int(prodtucto.precio))

        figura,ax = plt.subplots()
        ax.set_title("Productos con Mas Ingresos")
        ax.set_xlabel("Productos")
        ax.set_ylabel("Ingreso")
        ax.bar(nombres,ingresos)
        for i,txt in enumerate(ingresos):
            ax.annotate(txt,(i,ingresos[i]),textcoords="offset points",xytext=(0,10),ha="center")
        canvas = FigureCanvasTkAgg(figura, master = root)
        canvas.draw()

        canvas.get_tk_widget().pack()



