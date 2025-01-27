class Car:
    # Constructor (__init__) que inicializa los atributos del objeto
    def __init__(self, make, model, year):
        # Inicializamos los atributos con los valores proporcionados al crear el objeto
        self.make = make
        self.model = model
        self.year = year
        print(f"El coche {self.year} {self.make} {self.model} ha sido creado.")

    # Destructor (__del__) que realiza limpieza al destruir el objeto
    def __del__(self):
        # Este mét odo se llama cuando el objeto es destruido
        print(f"El coche {self.year} {self.make} {self.model} ha sido destruido.")

# Crear un objeto de la clase Car
my_car = Car("Toyota", "Corolla", 2020)

# El objeto se destruye cuando se sale del alcance, es decir, cuando termina la ejecución del programa
# El destructor se llama automáticamente en este momento.
del my_car  # Opcionalmente, podemos llamar a __del__ explícitamente, aunque no es necesario.

# También se puede utilizar el manejador de contexto `with` para manejar recursos, por ejemplo, con archivos
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        # Intentamos abrir el archivo al crear el objeto
        self.file = open(self.filename, 'w')
        print(f"Archivo {self.filename} abierto para escritura.")

    def write_data(self, data):
        # Escribimos datos en el archivo
        self.file.write(data)
        print("Datos escritos en el archivo.")

    def __del__(self):
        # Aseguramos que el archivo se cierre correctamente cuando el objeto sea destruido
        if self.file:
            self.file.close()
            print(f"Archivo {self.filename} cerrado.")

# Crear un objeto FileHandler y escribir datos en el archivo
file_handler = FileHandler("example.txt")
file_handler.write_data("¡Hola, mundo!")

# El objeto file_handler se destruye y el archivo se cierra al finalizar el programa o cuando se llama a __del__
del file_handler
