def quebracabecas(lista_pecas):
    '''Retorna o numero faltante
    '''
    n = len(lista_pecas) + 1
    somatotal = n * (n + 1) // 2
    return somatotal - sum(lista_pecas)