def maiores(lista,n):
    '''Esta função dada uma lista e um inteiro n retorna uma nova lista que contém somente os elementos maiores que esse inteiro da outra lista.
list,int-> list'''
    lista.insert(0,n)
    list.sort(lista)
    a=list.index(lista,n)
    lista_nova= lista[a+1:]
    return lista_nova