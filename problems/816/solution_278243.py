def maiores(lista, n):
    '''retorna a lista dada só com o números maiores que n'''
    lista.append(n)
    lista.sort()
    lista.reverse()
    p=lista.index(n)
    listaf= lista[:p]
    listaf.sort()
    return listaf