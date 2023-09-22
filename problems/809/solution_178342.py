def intercala(lista1, lista2):
    """intercala os elementos da primeira lista com os elementos da segunda lista;
    lista, lista -> lista"""
    l1 = lista1
    l2 = lista2
    return [[l1[0]] + [l2[0]] + [l1[1]] + [l2[1]] + [l1[2]] + [l2[2]]]