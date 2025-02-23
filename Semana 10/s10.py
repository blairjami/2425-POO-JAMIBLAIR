import os
import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(data["id_producto"], data["nombre"], data["cantidad"], data["precio"])

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        if not os.path.exists(self.archivo):
            return
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.productos = [Producto.from_dict(p) for p in data]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error al leer el archivo: {e}. Se iniciará con un inventario vacío.")
        except PermissionError:
            print("Error: No tienes permiso para leer el archivo de inventario.")

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump([p.to_dict() for p in self.productos], f, indent=4)
        except PermissionError:
            print("Error: No tienes permiso para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"Error desconocido al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("Error: El ID del producto ya existe en el inventario.")
        else:
            self.productos.append(producto)
            self.guardar_en_archivo()
            print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        self.guardar_en_archivo()
        print("Producto eliminado si existía.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if nueva_cantidad is not None:
                    producto.cantidad = nueva_cantidad
                if nuevo_precio is not None:
                    producto.precio = nuevo_precio
                self.guardar_en_archivo()
                print("Producto actualizado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")

def menu():
    inventario = Inventario()
    while True:
        print("\nSistema de Gestión de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID único: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
            precio = input("Nuevo precio (dejar vacío si no cambia): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
