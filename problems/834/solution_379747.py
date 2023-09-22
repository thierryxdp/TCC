def media_matriz(matriz):
    dividendo = 0
    divisor = 0
    for linha in matriz:
        for elemento in linha:
            dividendo += elemento
            divisor += 1
    return (dividendo/divisor)