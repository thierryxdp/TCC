def maiores(lista,n):
    '''
    lista, int -> lista'''
    list.insert(lista,0,n)
    list.sort(lista)
    lista2 = lista[0:n]
    return lista - lista2