def maiores(lista, n):
    '''Função que retorna outra lista que contenha todos os
    números da lista original maiores que n.
    lista=list,n=int->list'''
    lista2 = lista[n::+1]
    return lista2