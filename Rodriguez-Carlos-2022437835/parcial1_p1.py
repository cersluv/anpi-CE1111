import numpy as np
# parte a)
# entrada: A una matriz de tamaño nxn
#          d un vector de tamaño n
# Salida: x
# Restricciones: la matriz debe de tener valores reales, además de que ambas entradas deben de tener la misma cantidad
# de filas
def metodo_thomas(A, d):
    n = len(d)
    # Creación de los vectores a b y c vacíos
    a = np.zeros(n - 1)  # Diagonal inferior
    b = np.zeros(n)  # Diagonal
    c = np.zeros(n - 1)  # Diagonal superior

    for i in range(n):
        b[i] = A[i, i] # Diagonal
        if i < n - 1:
            a[i] = A[i + 1, i]  # Diagonal inferior
            c[i] = A[i, i + 1]  # Diagonal superior

    #  Creación de los vectores q y p

    p = np.zeros(n - 1)
    q = np.zeros(n)

    # Calcular p y q cuando i = 1
    p[0] = c[0] / b[0]
    q[0] = d[0] / b[0]

    # Calcular p y q cuando i es distinto de 1 [2, 3, ... n]
    for i in range(1, n - 1):
        denominador = b[i] - p[i - 1] * a[i - 1] # necesario hacerlo acá, por que un valor se vuelve tan grande que excede la capacidad del tipo de dao utilzado (float64)
        # solución al error sacada de https://stackoverflow.com/questions/7559595/python-runtimewarning-overflow-encountered-in-long-scalars
        p[i] = c[i] / denominador
        q[i] = (d[i] - q[i - 1] * a[i - 1]) / denominador

    q[n - 1] = (d[n - 1] - q[n - 2] * a[n - 2]) / (b[n - 1] - p[n - 2] * a[n - 2])

    x = np.zeros(n)
    x[-1] = q[-1]
    for i in range(n - 2, -1, -1):
        x[i] = q[i] - p[i] * x[i + 1]
    return x


# Pregunta (b)
# se crea la matriz A y el vector d
n = 250
A = np.zeros((n, n))
d = np.zeros(n)

# llenar A
for i in range(n):  # empieza en 0
    A[i, i] = 2 * (i + 1) # Diagonal
    if i < n - 1:
        A[i, i + 1] = i # Diganonal superior
        A[i, i - 1] = i # Digonal inferior
    d[i] = i + 1  # llenar el vector d


# Calcular x
x = metodo_thomas(A, d)

# Calcular el error ∥Ax - d∥2
error = np.linalg.norm(np.dot(A, x) - d, 2)
print("El error del cálculo de la solución es: ")
print(error)
