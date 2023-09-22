def conta_numero(numero, matriz):
    ''' Retorna a quantidade de vezes que o numero aparece na matriz'''
    c = 0
    for l in matriz:
        c +=  l.count(numero)
    return c