def conta_numero(numero, matriz):
    c = 1
    for i in range(len(matriz)):
        c = list.count(matriz[c], numero)
    c = c + 1
    return c