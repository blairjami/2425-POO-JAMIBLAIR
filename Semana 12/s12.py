import json


class Libro:
    def __init__(self, isbn, titulo, autor, categoria, prestado=False):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.prestado = prestado

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "prestado": self.prestado
        }


class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = []

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "libros_prestados": self.libros_prestados
        }


class Biblioteca:
    def __init__(self, archivo_libros='libros.json', archivo_usuarios='usuarios.json'):
        self.archivo_libros = archivo_libros
        self.archivo_usuarios = archivo_usuarios
        self.libros = self.cargar_datos(archivo_libros, Libro)
        self.usuarios = self.cargar_datos(archivo_usuarios, Usuario)

    def cargar_datos(self, archivo, clase):
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
                return {key: clase(**value) for key, value in datos.items()}
        except FileNotFoundError:
            return {}

    def guardar_datos(self, archivo, datos):
        with open(archivo, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in datos.items()}, f, indent=4)

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        self.guardar_datos(self.archivo_libros, self.libros)
        print(f"Libro '{libro.titulo}' añadido correctamente.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print("El usuario ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.guardar_datos(self.archivo_usuarios, self.usuarios)
            print(f"Usuario '{usuario.nombre}' registrado correctamente.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and not self.libros[isbn].prestado:
            if id_usuario in self.usuarios:
                self.libros[isbn].prestado = True
                self.usuarios[id_usuario].libros_prestados.append(isbn)
                self.guardar_datos(self.archivo_libros, self.libros)
                self.guardar_datos(self.archivo_usuarios, self.usuarios)
                print(f"Libro '{self.libros[isbn].titulo}' prestado a {self.usuarios[id_usuario].nombre}.")
            else:
                print("Usuario no registrado.")
        else:
            print("Libro no disponible.")

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario in self.usuarios and isbn in self.usuarios[id_usuario].libros_prestados:
            self.libros[isbn].prestado = False
            self.usuarios[id_usuario].libros_prestados.remove(isbn)
            self.guardar_datos(self.archivo_libros, self.libros)
            self.guardar_datos(self.archivo_usuarios, self.usuarios)
            print(f"Libro '{self.libros[isbn].titulo}' devuelto por {self.usuarios[id_usuario].nombre}.")
        else:
            print("Error en la devolución del libro.")

    def mostrar_libros(self):
        for libro in self.libros.values():
            estado = "Prestado" if libro.prestado else "Disponible"
            print(f"{libro.isbn}: {libro.titulo} por {libro.autor} - {estado}")

    def buscar_libro(self, criterio):
        resultados = [libro for libro in self.libros.values() if
                      criterio.lower() in libro.titulo.lower() or criterio.lower() in libro.autor.lower() or criterio.lower() in libro.categoria.lower()]
        if resultados:
            for libro in resultados:
                estado = "Prestado" if libro.prestado else "Disponible"
                print(f"{libro.isbn}: {libro.titulo} por {libro.autor} - {estado}")
        else:
            print("No se encontraron libros con ese criterio.")


def menu():
    biblioteca = Biblioteca()
    while True:
        print(
            "\n1. Añadir Libro\n2. Registrar Usuario\n3. Mostrar Libros\n4. Prestar Libro\n5. Devolver Libro\n6. Buscar Libro\n7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            biblioteca.añadir_libro(Libro(isbn, titulo, autor, categoria))
        elif opcion == '2':
            id_usuario = input("ID del usuario: ")
            nombre = input("Nombre del usuario: ")
            biblioteca.registrar_usuario(Usuario(id_usuario, nombre))
        elif opcion == '3':
            biblioteca.mostrar_libros()
        elif opcion == '4':
            isbn = input("ISBN del libro a prestar: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.prestar_libro(isbn, id_usuario)
        elif opcion == '5':
            isbn = input("ISBN del libro a devolver: ")
            id_usuario = input("ID del usuario: ")
            biblioteca.devolver_libro(isbn, id_usuario)
        elif opcion == '6':
            criterio = input("Ingrese título, autor o categoría a buscar: ")
            biblioteca.buscar_libro(criterio)
        elif opcion == '7':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()