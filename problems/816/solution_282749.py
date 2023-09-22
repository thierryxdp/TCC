def maiores(lista,n):
    ''' funcao recebe uma lista e um int, e retorna os elementos maiores que n, list,int-->list'''
    list.insert(lista,0,n)
    list.sort(lista)
    return lista[list.index(lista,n)+1:]