def conta_numero(numero, matriz):
    c = 0
    b = 0
    while b<len(matriz):
        a = list.count(matriz[b],numero)
        c=c+a
        b=b+1
    return c