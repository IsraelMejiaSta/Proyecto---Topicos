from tkinter import messagebox
import tkinter as tk

import cliente


class articulo:
    def __init__(self, id =0,nombre="",precio="",cantidad=""):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return (f" ID Producto:{self.id}\n"
                f"Nombre Producto: {self.nombre}\n"
                f"Precio: ${self.precio}\n"
                f"Cantidad: {self.cantidad}\n")
    @staticmethod
    def mostrarProducto(lista):
        for i in lista:
            print(i)
    @staticmethod
    def modificarProducto(frame,listaProductos,id):
        producto=None

        def modify():
            for i in listaProductos:
                if i.id == id:
                    i.nombre = nom.get()
                    i.precio = int(prec.get())
                    i.cantidad = int(cant.get())
                    messagebox.showinfo(message="Producto Modificado Correctamente")
        for n in listaProductos:
            if n.id == id:
                tk.Label(frame, text="Id Producto").pack()
                tk.Label(frame, text=n.id).pack()

                tk.Label(frame, text="Nombre").pack()
                nom = tk.Entry(frame)
                nom.pack()
                nom.insert(0,n.nombre)

                tk.Label(frame, text="Precio").pack()
                prec = tk.Entry(frame)
                prec.pack()
                prec.insert(0,n.precio)

                tk.Label(frame, text="Cantidad").pack()
                cant = tk.Entry(frame)
                cant.pack()
                cant.insert(0,n.cantidad)

                tk.Button(frame, text="Aceptar", command=modify).pack()


    @staticmethod
    def eliminarProducto(root,eliminarFrame,listaProductos,id):
        productoEliminar = None

        for i in listaProductos:
            if i.id == id:
                productoEliminar = i
                break

        if productoEliminar:
            listaProductos.remove(productoEliminar)
            messagebox.showinfo(message="Producto Eliminado")
        else:
            messagebox.showerror(message="Producto no encontrado")
        eliminarFrame.pack_forget()
        frameEliminar = tk.Frame(root)



    def stockBajo(self,listaProductos):
        for product in listaProductos:
            if product.cantidad <=5:
                print(product.id,product.nombre,product.precio,product.cantidad)



