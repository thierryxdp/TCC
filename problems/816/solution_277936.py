def maiores(lista,n):
    """ dada uma 'lista' e um número inteiro 'n', retorna outra lista que contém
    todos os elementos da lista original maiores que 'n'.
    list, n -> list """
    list.append(lista,n)
    list.sort(lista)
    a = list.index(lista,n)
    lista[a:]
    return a