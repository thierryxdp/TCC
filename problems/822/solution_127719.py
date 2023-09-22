def repetidos(lista):
    ''' função que retorna o número de vezes que um elemento  é igual ao elemento anterior
    list -> int
    '''
    i = 1
    x = 0
    while len(lista) > x:
        if lista[i] == lista[x - 1]:
            x += 1
            i += 1
        else:
            i += 1
    return x