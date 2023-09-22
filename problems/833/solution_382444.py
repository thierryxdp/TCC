def conta_numero(numero,matriz):
    '''Conta e retorne quantas vezes um número aparece na matriz; int,list->int'''
    contador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==numero:
                contador=contador+1
    return contador