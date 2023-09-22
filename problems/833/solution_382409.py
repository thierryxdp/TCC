def conta_numero(numero,matriz):
    '''Quanta a quantidade de vezes que um numero apareceu em uma matriz
       int, list -> int'''
    n = 0
    for i in matriz:
        for j in i:
            if j == numero:
                n += 1
    return n