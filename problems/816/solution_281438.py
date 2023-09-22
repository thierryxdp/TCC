def maiores(lista_numeros,n):
    """funcao que, dado uma lista de numeros inteiros e um numero inteiro n,
    retorna outra lista, a qual contenha todos os numeros da lista original maiores que n;
    list, int -> list"""
    lista_numeros+=[n]
    lista_numeros=list.sort(lista_numeros)
    return lista_numeros[:(list.index(lista_numeros,n))]