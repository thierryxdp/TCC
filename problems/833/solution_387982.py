def conta_numero(n,matriz):
    ''' Conta a quantidade de vezes que um número aparece em uma matriz.
    int,matriz => int'''
    repetiu = 0
    for int in range(0, len(matriz)):
        repetiu+=1 if len(matriz) == n else repetiu

    return repetiu