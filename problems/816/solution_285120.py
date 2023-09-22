def maiores (lista1,n):
    '''retorna uma lista em ordem crescentes dos valores maiores de n na lista lista1
    list,int->list'''
    list.append(lista1,n)
    list.sort(lista1)
    list.reverse(lista1)
    a=list.index(lista1,n)
    del lista1[-1,n-1]
    list.reverse(lista1)
    return lista1