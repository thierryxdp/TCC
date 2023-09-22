def conta_numero(numero,matriz):
    '''Conta e retorna quantas vezes um número qualquer aparece na matriz.
    int, list -> int'''
    elem = 0 
    i = len(matriz)
    j = len(matriz[0])
    for i and j in matriz:
        if i or j == numero:
            elem = elem + 1
    return elem