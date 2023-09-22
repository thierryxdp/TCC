def conta_numero(n,matriz):
    '''Retorna quantas vezes o número n apareceu na matriz.
    int, list -> int'''
    quantidade = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == n:
                quantidade = quantidade + 1
    return quantidade