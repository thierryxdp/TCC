def conta_numeros(numero, matriz):
    c = 0
    for linha in len(matriz):
        a = list.count(matriz[linha],numero)
        c=c+a
    return c