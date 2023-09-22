def maiores(lista,n):
    '''Dado uma lista de numeros inteiros e um numero inteiro n, retorna outra
    lista que contenha todos os numeros da lista original maiores que n.'''
    lista=lista+[n]
    indice=list.index(lista,n)
    return lista[indice:]