def conta_numero(numero, matriz):
    ''''''
    c=0
    c2=0
    for i in range(len(matriz[c2])):
        if i == numero:
            c=c+1
            c2=c2+1
    return c