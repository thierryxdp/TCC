def conta_numero(n,matriz):
    ''' Conta a quantidade de vezes que um número aparece em uma matriz.
    int,matriz => int'''
    repetiu = 0
    for indice in range(0, len(matriz)):
        repetiu+=1 if matriz[i,j] == n else repetiu

    return repetiu