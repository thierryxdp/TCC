def maiores(lista, n):
    '''função que faz retornar uma lista'''
    '''list, int -> list'''
    list.insert(lista,0,n)
    list.sort(lista)
    local_de_n = list.index(lista,n)
    lista = lista[local_de_n+1:]
    return lista