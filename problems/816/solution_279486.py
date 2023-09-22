def maiores(lista,n):
    """função que dada uma lista de numeros inteiros e um numero inteiro n retorne outra lista que contenha todos os numeros da lista original maiores que n; list, int-> list"""
    lista.append(n)
    lista.index(n)
    lista.sort()
    return lista