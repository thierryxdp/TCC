def conta_numero([numero, matriz]):
    '''Retorna o número de vezes que um dado número se encontra na matriz dada;
    int, list(list) -> int'''
    n = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                n = n + 1
    return n