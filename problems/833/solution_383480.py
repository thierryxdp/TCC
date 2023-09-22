def conta_numero(numero, matriz):
    c = 0
    for i in matriz[c]:
        c = c + 1
    return list.count(matriz[c], numero)