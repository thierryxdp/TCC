def conta_numero(numero, matriz):
    c = 0
    for i in range(matriz):
        c = list.count(matriz[c], numero)
    return c