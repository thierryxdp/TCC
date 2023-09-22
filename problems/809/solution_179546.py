def intercala(lista1, lista2):
    """ docs
    list, list -> list """

    a = lista1[0]
    b = lista1[1]
    c = lista1[2]
    d = lista2[0]
    e = lista2[1]
    f = lista2[2]
    
    lista1 = [a, b, c]
    lista2 = [d, e, f]

    return lista1 + lista2