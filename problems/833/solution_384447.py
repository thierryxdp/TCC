def conta_numero(numero, matriz):
    '''conta quantas vezes um numero aparece em uma matriz
    int, [[]] -> int'''
    
    nCol = len(matriz)
    nLin = len(matriz[0])
    
    vezes = 0
    for i in list(range(nCol)):
        for j in list(range(nLin)):
            if (numero == matriz[i][j]):
                vezes = vezes + 1
    
    return vezes