def filtraMultiplos(lista, n):
    """ A função filtra os múltiplos de n, retornando-os
	em uma nova lista;
    list, int -> list"""
    i = 0
    newlist = []
    while i < len(lista):
        if lista[i]%n == 0:
            list.append(newlist, lista[i])
        i += 1
    return newlist