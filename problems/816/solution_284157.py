def maiores(lista, n):
    '''Retorna uma lista com os número maiores que n
    presentes na lista original
    list, int --> list'''
    if n in lista:
        list.sort(lista)
        indice = list.index(lista, n)
        maiores = lista [indice + 1:]
        return maiores
    else:
        list.append(lista, n)
        list.sort(lista)
        indice = list.index(lista, n)
        maiores = lista [indice + 1:]
        return maiores