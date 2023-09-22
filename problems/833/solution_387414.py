def conta_numero(numero, matriz):
    '''conta quantas vezes um numero aparece numa matriz
    int, list(list) -> int'''
    repete = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                repete += 1
                return repete