def filtraMultiplos(l, n):
    '''filtra todos os números da lista(l) divisíveis por n
    list, int -> list'''
    i = 0
    lista = []
    while i < len(l):
		if l[i] % n == 0:
            list.append(lista, l[i])
        i += 1
    return lista