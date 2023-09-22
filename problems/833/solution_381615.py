def conta_numero(matriz,n):
    '''Função que, dada uma matriz e um número, retorna a quantidade de vezes que esse número aparece na matriz.
    list, int --> int'''
    quantidade = 0
    for x in matriz:
        for y in x:
            if matriz[list.index(matriz,x)][list.index(x,y)] == n:
                quantidade = quantidade + 1
    return quantidade