def conta_numero(numero, matriz):
    c = 0
    for linha in len(matriz):
        a = list.count(matriz[linha],numero)
        c=c+a
    return c