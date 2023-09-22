def maiores(lista, n):
    '''Funçao que dada uma lista e um número inteiro, retornará uma outra lista com apenas os números maiores que 'n'.
    list, int->list'''
    list.insert(lista,0, n)
    list.sort(lista)
    i=list.index(lista, n)
    return lista[i+1:]