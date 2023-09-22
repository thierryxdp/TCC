def conta_numero(numero, matriz):
    x = 0
    y = 0
    for lista in matriz:
        y = y + list.count(matriz[x], numero)
        x = x + 1
    return y