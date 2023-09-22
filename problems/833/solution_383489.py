def conta_numero(numero, matriz):
    c = 1
    for i in matriz:
        c = list.count(matriz[c], numero)
    return c