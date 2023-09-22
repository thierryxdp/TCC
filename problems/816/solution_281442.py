def maiores(lista_numeros,n):
    """funcao que, dado uma lista de numeros inteiros e um numero inteiro n,
    retorna outra lista, a qual contenha todos os numeros da lista original maiores que n;
    list, int -> list"""
    a=lista_numeros
    a+=[n]
    a.sort()
    list.reverse(a)
    return a[:(list.index(a,n))]