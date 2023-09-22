def maiores(lista,n):
    '''
    lista, int -> lista'''
    list.insert(lista,0,n)
    list.sort(lista)
    return list.pop(lista[0:n+1])