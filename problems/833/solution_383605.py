def conta_numero(numero, matriz):
    c = 0
    for x in range(len(matriz)):
        c = c + list.count(matriz[x], numero)
    return c