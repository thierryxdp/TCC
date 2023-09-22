def intercala(lista1, lista2):
    lista1 = list()
    lista2 = list()
    res = lista1 + lista2
    res[::2] = lista1
    res[1::2] = lista2
    return str(res)