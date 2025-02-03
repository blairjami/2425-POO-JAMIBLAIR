# Programación Tradicional

def ingresar_temperaturas():
    temperaturas = []
    for dia in range(7):
        temp = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Ejecución del programa en programación tradicional
temperaturas = ingresar_temperaturas()
promedio = calcular_promedio(temperaturas)
print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")
