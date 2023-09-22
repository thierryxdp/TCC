def faltante(lista):
    '''
    Dado uma lista com N-1 números inteiros numerados de 1
    a N, determina o número faltante.
    list->int
    '''
    list.sort(lista)
    if 1 not in lista:
        return 1
    if lista[-1] < len(lista) + 1:
        return len(lista) + 1
    x = 0
    faltante = 0
    while x < len(lista) - 1:
        if lista[x + 1] - lista[x] > 1:
            faltante = faltante + lista[x] + 1
        x = x + 1
    return faltante