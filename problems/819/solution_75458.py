def filtraMultiplos(lista, n):
    '''Filtra os múltiplos do número n.
    lista, int -> lista'''
    listaMult = ()
    for item in lista:
        if item % n == 0:
            listaMult.append(item)
    return listaMult