def filtraMultiplos(l, n):
    '''
    A função retorna uma lista contendo os multiplos
    de um número em uma lista
    (entrada = list / saída = list)
    '''
    ln = []
    for x in l:
        if l[x] % n:
            ln += l[x]
    return ln