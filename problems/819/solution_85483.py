def filtraMultiplos(lista_num, n):
    """função que dada uma lista e um numero, retorna uma lista que possui os elementos da primeira lista divisiveis por n.
    list, int -> list"""
    lista = ()
    i = 0
    while i < len(lista_num):
        if int(lista_num[i]) % n == 0:
            lista = lista + (lista_num[i],)
        i = i + 1
    return list(lista)