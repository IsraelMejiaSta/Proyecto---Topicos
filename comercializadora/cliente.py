import tkinter as tk
from tkinter import messagebox


class Cliente:
    def __init__(self,id=0, nombre="",apellidoPaterno="",apellidoMaterno="",telefono="",direccion="",correo=""):
        self.id = id
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

    def __str__(self):
        return (f"ID Cliente: {self.id}\n"
                f"Nombre Cliente: {self.nombre}\n"
                f"Apellido Paterno: {self.apellidoPaterno}\n"
                f"Apellido Materno: {self.apellidoMaterno}\n"
                f"Telefono: {self.telefono}\n"
                f"Direccion: {self.direccion}\n"
                f"correo: {self.correo}\n")


    def limpiarCampos(self, frame):
        for widget in frame.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)

    def modificarCliente(self, idC,listaCliente,frame):

        def modify():
            for i in listaCliente:
                if i.id == idC:
                    i.nombre = nom.get()
                    i.apellidoPaterno = aPaterno.get()
                    i.apellidoMaterno = aMaterno.get()
                    i.telefono = cel.get()
                    i.direccion = calle.get()
                    i.correo = email.get()
                    messagebox.showinfo(message="Cliente modificado Correctamente")
                    self.limpiarCampos(frame)
        for i in listaCliente:
            if i.id == idC:
                tk.Label(frame, text="Que Deceas Modificar").pack()

                tk.Label(frame, text="id CLiente").pack()
                tk.Label(frame, text=i.id).pack()

                tk.Label(frame, text="Nombre").pack()
                nom = tk.Entry(frame)
                nom.pack()
                nom.insert(tk.END, i.nombre)

                tk.Label(frame, text="Apellido Paterno").pack()
                aPaterno = tk.Entry(frame)
                aPaterno.pack()
                aPaterno.insert(tk.END, i.apellidoPaterno)

                tk.Label(frame, text="Apellido Materno").pack()
                aMaterno = tk.Entry(frame)
                aMaterno.pack()
                aMaterno.insert(tk.END, i.apellidoMaterno)

                tk.Label(frame, text="Telefono").pack()
                cel = tk.Entry(frame)
                cel.pack()
                cel.insert(tk.END, i.telefono)

                tk.Label(frame, text="Direccion").pack()
                calle = tk.Entry(frame)
                calle.pack()
                calle.insert(tk.END, i.direccion)

                tk.Label(frame, text="Correo Electronico").pack()
                email = tk.Entry(frame)
                email.pack()
                email.insert(tk.END, i.correo)

                tk.Button(frame, text="Modificar", command=modify).pack()





    def eliminarCliente(self,listaCliente,id):
        id -= 1
        listaCliente.remove(listaCliente[id])


