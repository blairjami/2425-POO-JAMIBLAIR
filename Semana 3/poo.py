# Programación Orientada a Objetos (POO)

class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for dia in range(7):
            temp = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Ejecución del programa en POO
clima = ClimaSemanal()
clima.ingresar_temperaturas()
promedio_poo = clima.calcular_promedio()
print(f"El promedio semanal de temperaturas (POO) es: {promedio_poo:.2f} °C")
