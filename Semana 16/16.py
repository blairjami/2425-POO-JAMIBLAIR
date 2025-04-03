import tkinter as tk
from tkinter import messagebox

def agregar_tarea(event=None):
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía.")

def marcar_completada(event=None):
    try:
        seleccion = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(seleccion)
        if not tarea.startswith("✔ "):
            lista_tareas.delete(seleccion)
            lista_tareas.insert(seleccion, "✔ " + tarea)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

def eliminar_tarea(event=None):
    try:
        seleccion = lista_tareas.curselection()[0]
        lista_tareas.delete(seleccion)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

def cerrar_app(event=None):
    root.quit()

# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("400x300")

# Campo de entrada y botón de agregar
entrada_tarea = tk.Entry(root, width=40)
entrada_tarea.pack(pady=10)
entrada_tarea.bind("<Return>", agregar_tarea)

btn_agregar = tk.Button(root, text="Agregar Tarea", command=agregar_tarea)
btn_agregar.pack()

# Lista de tareas
lista_tareas = tk.Listbox(root, width=50, height=10)
lista_tareas.pack(pady=10)

# Botones de acción
btn_completar = tk.Button(root, text="Marcar Completada", command=marcar_completada)
btn_completar.pack()
btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack()

# Configuración de atajos de teclado
root.bind("<c>", marcar_completada)
root.bind("<d>", eliminar_tarea)
root.bind("<Delete>", eliminar_tarea)
root.bind("<Escape>", cerrar_app)

# Ejecutar aplicación
root.mainloop()
