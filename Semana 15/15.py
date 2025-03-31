import tkinter as tk
from tkinter import messagebox

def agregar_tarea(event=None):
    tarea = entry_tarea.get()
    if tarea:
        listbox_tareas.insert(tk.END, tarea)
        entry_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Ingrese una tarea antes de añadir.")

def marcar_completada():
    try:
        seleccion = listbox_tareas.curselection()[0]
        tarea = listbox_tareas.get(seleccion)
        listbox_tareas.delete(seleccion)
        listbox_tareas.insert(seleccion, f"✔ {tarea}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

def eliminar_tarea():
    try:
        seleccion = listbox_tareas.curselection()[0]
        listbox_tareas.delete(seleccion)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

# Configuración de la ventana
root = tk.Tk()
root.title("Lista de Tareas")

# Campo de entrada
entry_tarea = tk.Entry(root, width=50)
entry_tarea.pack(pady=10)
entry_tarea.bind("<Return>", agregar_tarea)  # Permitir añadir tarea con Enter

# Botones
frame_botones = tk.Frame(root)
frame_botones.pack()

btn_agregar = tk.Button(frame_botones, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.grid(row=0, column=0, padx=5)

btn_completar = tk.Button(frame_botones, text="Marcar como Completada", command=marcar_completada)
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.grid(row=0, column=2, padx=5)

# Lista de tareas
listbox_tareas = tk.Listbox(root, width=50, height=10)
listbox_tareas.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()