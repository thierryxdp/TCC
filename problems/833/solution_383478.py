def conta_numero(numero, matriz):
    c = 0
    for i in matriz[c]:
        c = list.count(matriz[c], numero)
    return c