def maiores(lista_numero, n):
    '''Retorna uma lista com todos os números maiores que n.
    list, int -> list'''
    lista = lista_numero+[n]
    list.sort (lista)
    pos = list.index(lista,n)
    return lista[pos+1:]