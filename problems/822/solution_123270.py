def repetidos(l):
    '''Retorna o numero de vezes que um elemento da lista é igual ao seu anterior.'''
    i = 1
    r = 0
    while i < len(l):
        if l[i] == l[i-1]:
            r = r + 1
        i = i + 1
    return r