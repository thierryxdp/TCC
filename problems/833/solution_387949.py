def conta_numero(n,matriz):
    ''' Conta a quantidade de vezes que um número aparece em uma matriz.
    int,matriz => int'''
    contador - 0
    for i in range(len(matriz)):
        for j in range(i):
            if matriz[i][j] = n:
                contador = contador + 1
        return contador