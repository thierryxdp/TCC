def conta_numero(matriz,n):
    ''' retorna quantas vezes um numero aparece na matriz
    list, int -> int
    '''
    contador = 0
    for i in matriz:
        for k in i:
            if k == n:
                contador += 1
    return contador