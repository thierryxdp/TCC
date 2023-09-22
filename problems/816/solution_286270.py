def maiores(lista, n):
    '''Retorna uma lista com os números de lista maiores que n
     list, int -> list'''
    ind = list.index(list.sort(lista), n)
    return lista[ind+1:]