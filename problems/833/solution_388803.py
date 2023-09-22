def conta_numero(numero, matriz):
    lin = len(matriz)
    col = len(matriz[0])
    qtd = 0
    for i in range(lin):
        if numero in matriz[0][i]:
            qnt+=1
    return qtd