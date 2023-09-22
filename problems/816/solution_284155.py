def maiores(lista, n):
    '''Retorna uma lista com os número maiores que n
    presentes na lista original
    list, int --> list'''
    if n in lista:
        list.sort(lista)
        índice = list.index(lista, n)
        maiores = lista [índice + 1:]
        return maiores
    else:
        list.append(lista, n)
        list.sort(lista)
        índice = list.index(lista, n)
        maiores = lista [índice + 1:]
        return maiores