def conta_numero(numero, matriz):
    ''' A função conta_numero, dado um número inteiro e 
    uma matriz de inteiros de tamanho qualquer, conta e 
    retorna quantas vezes aquele número aparece na matriz.
    int, list --> int
    '''
    nlin = len(matriz)
    if nlin == 0:
        return 0
    ncol = len(matriz[0])
    contador = 0
    for i in range(nlin):
        for j in range(ncol):
            if numero == matriz[i][j]:
                contador += 1
    return contador