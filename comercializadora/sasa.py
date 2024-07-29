import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Crear la ventana principal
root = tk.Tk()
root.title("Gráfica en Tkinter")

# Crear un Frame para contener la gráfica
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Datos
x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]
y2 = [0, 1, 2, 3, 4, 5]

# Crear la figura de matplotlib
fig, ax = plt.subplots()
line1, = ax.plot(x, y1, label='Datos 1', color='blue', marker='o')
line2, = ax.plot(x, y2, label='Datos 2', color='red', marker='x')

# Añadir títulos y etiquetas
ax.set_title('Gráfica de dos conjuntos de datos')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.legend()

# Añadir anotaciones con la cantidad de cada dato
for i, txt in enumerate(y1):
    ax.annotate(txt, (x[i], y1[i]), textcoords="offset points", xytext=(0,10), ha='center')
for i, txt in enumerate(y2):
    ax.annotate(txt, (x[i], y2[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Crear el canvas de Tkinter para la figura de matplotlib
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()

# Colocar el canvas en el Frame
canvas.get_tk_widget().grid(row=0, column=0)

# Ejecutar el bucle principal de Tkinter
root.mainloop()
