def maiores (lista, n):
    '''função que, dada uma lista, retorna outra lista com elemnetos da original maiores que n
    list -> list'''
    lista = lista + [n]
    list.sort(lista)
    k = lista.index(n)
    lista = lista[k:] 
    lista.pop(0)
    return lista