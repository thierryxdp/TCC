def maiores(lista, n):
    '''retorna a lista ordenada excluindo valores maiores que n
    list, int'''
    list.append(lista,n)
    list.sort(lista)
    x=lista.index(n)
    lista_nova=lista[x:]
    list.remove(lista_nova, n)
    return lista_nova