def intercala(lista1, lista2):
    '''Intercala listas
    int, int -> str'''
    res = lista1 + lista2
    res[::2] = lista1
    res[1::2] = lista2
    return res