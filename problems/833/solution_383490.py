def conta_numero(numero, matriz):
    c = 2
    for i in matriz:
        c = list.count(matriz[c], numero)
    return c