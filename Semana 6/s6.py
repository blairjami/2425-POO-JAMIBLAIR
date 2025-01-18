# Ejemplo de programa en Python para aplicar POO

# Clase base: Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self._edad = edad     # Atributo protegido (Encapsulación)

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self._edad}"

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}."


# Clase derivada: Estudiante (hereda de Persona)
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.carrera = carrera          # Atributo adicional

    # Sobrescritura de métod,o(Polimorfismo)
    def saludar(self):
        return f"Hola, soy {self.nombre}, estudiante de {self.carrera}."


# Clase derivada: Profesor (hereda de Persona)
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    # Sobrescritura de métod,o (Polimorfismo)
    def saludar(self):
        return f"Buenos días, soy el profesor {self.nombre}, enseño {self.materia}."


# Ejemplo de encapsulación: modificar la edad de forma controlada
class PersonaConEncapsulacion(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad > 0:  # Validación simple
            self._edad = nueva_edad
        else:
            print("La edad debe ser un número positivo.")


# Instanciación de clases y demostración de funcionalidad
if __name__ == "__main__":
    # Creación de un objeto de la clase Persona
    persona = Persona("Ana", 30)
    print(persona.mostrar_informacion())
    print(persona.saludar())

    # Creación de un objeto de la clase Estudiante
    estudiante = Estudiante("Carlos", 20, "Ingeniería en Software")
    print(estudiante.mostrar_informacion())
    print(estudiante.saludar())

    # Creación de un objeto de la clase Profesor
    profesor = Profesor("Luis", 45, "Matemáticas")
    print(profesor.mostrar_informacion())
    print(profesor.saludar())

    # Encapsulación: Uso de getter y setter para modificar la edad
    persona_encapsulada = PersonaConEncapsulacion("María", 28)
    print(persona_encapsulada.mostrar_informacion())
    persona_encapsulada.edad = 35  # Uso del setter
    print(f"Edad actualizada: {persona_encapsulada.edad}")
    persona_encapsulada.edad = -5  # Intento de asignar un valor inválido
