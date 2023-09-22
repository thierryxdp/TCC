def conta_numero(numero, matriz):
    ''''''
    linha = len(matriz)
    coluna = len(matriz[0]) 
    c=0
    c2=0
    for i in range(len(matriz)):
        if i == numero:
            c=c+1
    return c