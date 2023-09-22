def intercala(lista1, lista2):
    """ entra duas listas e sai uma concatenada
    list -> list """
    l1 = lista1
    l2 = lista2
    l1.extend(l2)
    return l1