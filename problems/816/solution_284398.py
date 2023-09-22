def maiores(lista1,n):
    '''Retorna os valores da lista que são maiores que n
    str,int --> list'''
    lista1[0:0] = [n]
    list.sort(lista1)
    maior = lista1[(list.index(lista1,n))+1:]
    return maior