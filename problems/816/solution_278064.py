def maiores(lista,n):
    '''Funcao que dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista, que contenha todos os numeros da lista original maiores que n,
    lista, int -> lista'''
    list.insert(lista,0,n)
    list.sort(lista)
    return lista[list.index [(lista)+1:]]