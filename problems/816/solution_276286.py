def maiores(lista,n):
    '''função que recebe uma lista de números inteiros e um número
    n e retorna uma lista com números maiores que n.
    lista,int->list'''
    x=list.append(lista,n)
    y=list.sort(lista)
    z=list.index(lista,n)
    return lista[z+1:]