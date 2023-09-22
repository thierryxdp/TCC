def conta_numero(numero,matriz):
    """
    retorna quantas vezes o numero informado aparece na matriz
    """
    vezes=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                vezes+=1
    return vezes