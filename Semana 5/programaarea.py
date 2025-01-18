# Descripción del programa: Calcula el área de un círculo a partir del radio proporcionado por el usuario.
# Este programa utiliza diferentes tipos de datos: float para el radio, string para la entrada del usuario,
# y boolean para la validación de la entrada.

def calcular_area_circulo(radio):
    """
    Función para calcular el área de un círculo.
    :param radio: float, el radio del círculo
    :return: float, el área del círculo
    """
    import math
    area = math.pi * (radio ** 2)
    return area


def main():
    print("Bienvenido al cálculo del área de un círculo.")

    # Solicitar al usuario el radio del círculo
    while True:
        try:
            radio = float(input("Por favor, ingresa el radio del círculo: "))
            if radio > 0:
                break
            else:
                print("El radio debe ser un número positivo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    # Calcular el área
    area = calcular_area_circulo(radio)

    # Mostrar el resultado
    print(f"El área del círculo con radio {radio} es: {area:.2f} unidades²")


if __name__ == "__main__":
    main()
