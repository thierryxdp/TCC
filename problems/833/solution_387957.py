def conta_numero(n,matriz):
    ''' Conta a quantidade de vezes que um número aparece em uma matriz.
    int,matriz => int'''
    contador = 0
    for i in range(0,10):
        for j in range(0,10):
        if matriz[i][j] == n:
                contador = contador + 1
        return contador