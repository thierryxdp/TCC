def maiores(lista, n):
    ''' esta função recebe uma lista e retorna outra com so com os numeros maiores que n. list,int->list.'''
    if n in lista :
        list.sort(lista)
        l = l[list.index(lista,n)+1:]
        return l 
    else:
        lista.insert(-1,n)
        list.sort(lista)
        l = lista[list.index(lista,n)+1:]
        return l