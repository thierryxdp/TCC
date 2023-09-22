def media_matriz(matriz):
    n = 0
    numero_elementos = 0
    for linha in matriz:
        for elemento in linha:
            numero_elementos += 1
            n += elemento
    return round(n / numero_elementos, 2)