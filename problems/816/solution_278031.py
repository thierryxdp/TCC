def maiores(lista,n):
    '''
    lista, int -> lista'''
    list.insert(lista,0,n)
    list.sort(lista)
    return lista - lista[0:n]