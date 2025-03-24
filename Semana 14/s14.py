import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda Personal")

# Variables
eventos = []

# Función para agregar un evento
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha == "" or hora == "" or descripcion == "":
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
        return

    evento = (fecha, hora, descripcion)
    eventos.append(evento)
    actualizar_lista()

    entry_fecha.delete(0, tk.END)
    entry_hora.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)

# Función para eliminar un evento seleccionado
def eliminar_evento():
    try:
        seleccionado = lista_eventos.selection()[0]
        lista_eventos.delete(seleccionado)
        eventos.pop(lista_eventos.index(seleccionado))
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un evento para eliminar.")

# Función para actualizar la lista de eventos
def actualizar_lista():
    for item in lista_eventos.get_children():
        lista_eventos.delete(item)
    for evento in eventos:
        lista_eventos.insert("", tk.END, values=evento)

# Crear los widgets
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

label_fecha = tk.Label(frame_entrada, text="Fecha (DD/MM/AAAA):")
label_fecha.grid(row=0, column=0, padx=5)

entry_fecha = tk.Entry(frame_entrada)
entry_fecha.grid(row=0, column=1, padx=5)

label_hora = tk.Label(frame_entrada, text="Hora (HH:MM):")
label_hora.grid(row=0, column=2, padx=5)

entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=0, column=3, padx=5)

label_descripcion = tk.Label(frame_entrada, text="Descripción:")
label_descripcion.grid(row=1, column=0, padx=5)

entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=1, column=1, columnspan=3, padx=5)

boton_agregar = tk.Button(frame_entrada, text="Agregar Evento", command=agregar_evento)
boton_agregar.grid(row=2, column=0, columnspan=4, pady=10)

# Crear la lista de eventos
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

lista_eventos = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
lista_eventos.heading("Fecha", text="Fecha")
lista_eventos.heading("Hora", text="Hora")
lista_eventos.heading("Descripción", text="Descripción")
lista_eventos.pack()

# Botón para eliminar evento
boton_eliminar = tk.Button(root, text="Eliminar Evento Seleccionado", command=eliminar_evento)
boton_eliminar.pack(pady=10)

# Botón de salir
boton_salir = tk.Button(root, text="Salir", command=root.quit)
boton_salir.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
