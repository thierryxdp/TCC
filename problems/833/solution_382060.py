def conta_numero(numero,matriz):
    '''retorna quantas vezes um numero aparece na matriz. int,list(list)->int'''
    n = 0
    for x in len(matriz):
        for y in matriz[x]:
            if numero == y:
                n += 1
    return n