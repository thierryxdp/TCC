def media_matriz(matriz):
    dividendo = 0
    divisor = 0
    for linha in matriz:
        for elemento in linha:
            dividendo += elemento
            divisor += 1
    media = dividendo/divisor
    return round(2, media)