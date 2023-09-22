def maiores(lista,n):
    '''Retorna os valores da lista que são maiores que n
    str,int --> list'''
    lista[0:0] = [n]
    list.sort(lista)
    maiores = lista[(list.index(lista,n))+1:]
    return maiores