def maiores(lista,n):
    '''Função que que retorna a lista só com os numeros maiores que o indicado
list,int->list'''
    list.sort(lista)
    list.reverse(lista)
    del lista[list.index(lista, n):]
    list.reverse(lista)

    return lista