def maiores(lista, n):
    '''Retorna uma lista com os números de lista maiores que n
     list, int -> list'''
    list.sort(lista)
    ind = list.index(lista, n)
    return lista[ind+1:]