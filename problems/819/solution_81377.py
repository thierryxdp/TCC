def filtraMultiplos():
    """
    """
    lista = [2, 3, 1, 5, 1, 7, 8, 8, 9, 15, 1, 1]
    lista = list(filter(lambda x: x != 1, lista))
    return(lista)