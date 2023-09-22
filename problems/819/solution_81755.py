def filtraMultiplos(l, n):
    '''
    A função retorna uma lista contendo os multiplos
    de um número em uma lista
    (entrada = list / saída = list)
    '''
    ln = []
    i = 0
    while i < len(l):
        if l[i] % n == 0:
            ln += [l[i]]
        i += 1
    return ln