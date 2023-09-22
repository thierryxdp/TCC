import math
def soma_fatorial(n):
    fatorial = []
    numero = 0

    for i in range(1, n+1):
        numero = math.factorial(i)
        fatorial.append(numero)

    return sum(fatorial)