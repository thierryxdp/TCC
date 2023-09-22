def maiores(lista,n):
    '''uma função que dada uma lista e um número, retorna outra lista com todos numeros 
    da lista original maiores que n
    lista + int -> lista'''
    list.sort(lista)
    ba = list.index(lista, n)
    return lista[ba:)