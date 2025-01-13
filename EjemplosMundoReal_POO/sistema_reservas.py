# Clase para representar una habitación
class Habitacion:
    def __init__(self, numero, tipo, precio, esta_disponible=True):
        """
        Constructor de la clase Habitacion.
        :param numero: Número de la habitación.
        :param tipo: Tipo de habitación (Ej: 'Simple', 'Doble').
        :param precio: Precio por noche.
        :param esta_disponible: Estado de disponibilidad.
        """
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.esta_disponible = esta_disponible

    def cambiar_disponibilidad(self, disponible):
        """
        Cambia el estado de disponibilidad de la habitación.
        :param disponible: Nuevo estado (True o False).
        """
        self.esta_disponible = disponible


# Clase para representar una reserva
class Reserva:
    def __init__(self, cliente, habitacion, noches):
        """
        Constructor de la clase Reserva.
        :param cliente: Nombre del cliente.
        :param habitacion: Objeto Habitacion reservado.
        :param noches: Número de noches de la estancia.
        """
        self.cliente = cliente
        self.habitacion = habitacion
        self.noches = noches
        self.total = self.calcular_total()

    def calcular_total(self):
        """
        Calcula el costo total de la reserva.
        :return: Total en base al precio de la habitación y las noches.
        """
        return self.noches * self.habitacion.precio


# Clase para gestionar el sistema de reservas
class SistemaReservas:
    def __init__(self):
        """
        Constructor de la clase SistemaReservas.
        """
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, habitacion):
        """
        Añade una habitación al sistema.
        :param habitacion: Objeto Habitacion.
        """
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        """
        Muestra las habitaciones disponibles.
        """
        print("Habitaciones disponibles:")
        for habitacion in self.habitaciones:
            if habitacion.esta_disponible:
                print(f"Habitación {habitacion.numero} - {habitacion.tipo} - ${habitacion.precio}/noche")

    def realizar_reserva(self, cliente, numero_habitacion, noches):
        """
        Realiza una reserva si la habitación está disponible.
        :param cliente: Nombre del cliente.
        :param numero_habitacion: Número de la habitación a reservar.
        :param noches: Número de noches.
        """
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion and habitacion.esta_disponible:
                habitacion.cambiar_disponibilidad(False)
                nueva_reserva = Reserva(cliente, habitacion, noches)
                self.reservas.append(nueva_reserva)
                print(f"Reserva realizada para {cliente}. Total: ${nueva_reserva.total}")
                return
        print("Habitación no disponible o no encontrada.")

    def mostrar_reservas(self):
        """
        Muestra todas las reservas realizadas.
        """
        print("Reservas actuales:")
        for reserva in self.reservas:
            print(f"Cliente: {reserva.cliente} - Habitación: {reserva.habitacion.numero} - Total: ${reserva.total}")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear sistema de reservas
    sistema = SistemaReservas()

    # Agregar habitaciones
    sistema.agregar_habitacion(Habitacion(101, "Simple", 50))
    sistema.agregar_habitacion(Habitacion(102, "Doble", 80))
    sistema.agregar_habitacion(Habitacion(103, "Suite", 150))

    # Mostrar habitaciones disponibles
    sistema.mostrar_habitaciones_disponibles()

    # Realizar reservas
    sistema.realizar_reserva("Juan Pérez", 101, 3)
    sistema.realizar_reserva("Ana Gómez", 102, 2)

    # Mostrar habitaciones disponibles después de las reservas
    sistema.mostrar_habitaciones_disponibles()

    # Mostrar reservas actuales
    sistema.mostrar_reservas()
