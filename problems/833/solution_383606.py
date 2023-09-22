def conta_numero(numero, matriz):
    '''Conta quanats vezes um certo numero aparece na matriz.
    int , list -> int'''
    c = 0
    for x in range(len(matriz)):
        c = c + list.count(matriz[x], numero)
    return c