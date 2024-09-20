import numpy as np


def parcial1_p2():
    # Valor inicial, tolerancia e iteraciones máximas
    # Se utiliza un x0 de 4, después de observar la gráfica de la función
    x0 = 4
    tol = 1e-10
    max_iter = 1000

    # Función principal f(x)
    def f(x):
        return np.exp(x) - np.pi * x - np.log(x) - 50

    # Derivada de la función principal
    def derivada(x):
        return np.exp(x) - np.pi - 1/x

    xn = x0

    for n in range(max_iter):
        # Primero calculamos el valor inicial de zn, esto como: xn - f(x)/f'(x)
        zn = xn - f(xn) / derivada(xn)

        # Luego calculamos H con la fórmula del enunciado
        H = (derivada(xn) - derivada(zn)) / (3 * derivada(zn) - derivada(xn))

        # Se hace la iteración para obtener nuestro Xn+1
        xn1 = zn - H * (f(zn) / derivada(xn))

        # Comprobamos el criterio de parada
        if abs(f(xn1)) < tol:
            print(f"Aproximación del cero: {xn1}")
            print(f"Número de iteraciones: {n}")
            print(f"Error: {abs(f(xn1))}")
            return

        # Se actualiza xn para la siguiente iteración
        xn = xn1

    # Caso de fallo (normalmente ocurre cuando no se coloca un valor inicial no cercano)
    print("No se encontró una solución en las iteraciones dadas")
    print(f"Última aproximación: {xn}")
    print(f"Error: {abs(f(xn))}")

# Ejecutar la función
parcial1_p2()
