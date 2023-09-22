def conta_numero(numero, matriz):
    ''''''
    c=0
    c2=0
    for i in range(len(matriz[0])):
        if i in matriz[0]:
            c=c+1
    return c