def intercala(l1, l2):
    """ entra duas listas e sai uma concatenada
    list -> list """
    lista1 = l1
    lista2 = l2
    lista1.extend(lista2)
    return lista1