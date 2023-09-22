def maiores(lista, n):
    '''Função que retorna outra lista que contenha todos os
    números da lista original maiores que n.
    lista=list,n=int->list'''
    list.append(lista,n)
    list.sort(lista)
    x = list.index(lista,n)
    return lista[x+1:]