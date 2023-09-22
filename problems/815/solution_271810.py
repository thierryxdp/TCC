def insere(ln, n):
    '''
    A função retorna uma lista com os números em
    ordem crescente
    (entrada = list, int / saída = list)
    '''
    ln = ln + [n]
    list.sort(ln)
    return ln