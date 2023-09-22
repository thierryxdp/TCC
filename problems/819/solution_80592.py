def filtraMultiplos(listaNumeros,numeroN):
    '''Dada uma lista de números e um número n, retorna
    outra lista contendo todos os elementos da lista
    original que forem divisíveis por n.
    list, int -> list'''
    indice = 0
    listaMultiplos = []
    while indice < len(listaNumeros):
        if listaNumeros[indice]%numeroN==0:
            listaMultiplos = listaMultiplos + [listaNumeros[indice]]
        indice = indice + 1
    return listaMultiplos