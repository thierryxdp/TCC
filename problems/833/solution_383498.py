def conta_numero(numero, matriz):
    c = 1
    for i in range(matriz):
        c = list.count(matriz[c], numero)
    return c