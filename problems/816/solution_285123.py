def maiores (lista1,n):
    '''retorna uma lista em ordem crescentes dos valores maiores de n na lista lista1
    list,int->list'''
    list.append(lista1,n)
    list.sort(lista1)
    a=list.index(lista1,n)
    list.remove(lista1,lista1[0,a+1])
    return lista1