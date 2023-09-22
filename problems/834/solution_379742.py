def media_matriz(matriz):
    dividendo = sum(matriz)
    divisor = 0
    for linha in matriz:
        for elemento in linha:
            divisor += 1
    media = dividendo/divisor
    return round(2, media)