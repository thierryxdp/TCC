def conta_numero(numero,matriz):
    '''Conta e retorna quantas vezes um número qualquer aparece na matriz.
    int, list -> int'''
    elem = 0 
    i = len(matriz)
    j = len(matriz[0])
    for i in matriz:
        for j in matriz:
            if numero == j:
       		elem = elem + 1
    return elem