import random

# Función recursiva
def promedio(arreglo, i, minimo, maximo):

    # Caso base
    if i == len(arreglo):
        return (minimo + maximo) / 2

    # Verificar múltiplos de 3
    if arreglo[i] % 3 == 0:

        if arreglo[i] < minimo:
            minimo = arreglo[i]

        if arreglo[i] > maximo:
            maximo = arreglo[i]

    # Llamada recursiva
    return promedio(arreglo, i + 1, minimo, maximo)


# Programa principal

n = int(input("Ingrese tamaño del arreglo: "))

arreglo = []

# Llenar arreglo con números aleatorios
for i in range(n):
    arreglo.append(random.randint(10, 9999))

print(arreglo)

# Buscar primer múltiplo de 3
for num in arreglo:
    if num % 3 == 0:
        minimo = num
        maximo = num
        break

# Llamar función
resultado = promedio(arreglo, 0, minimo, maximo)

print("Resultado:", resultado)