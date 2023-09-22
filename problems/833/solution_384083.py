def conta_numero(numero,matriz):
    """ função que conta e retorna quantas vezes aquele numero aparece na matriz; int, int-> int"""
    c=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                c=c+1
    return c