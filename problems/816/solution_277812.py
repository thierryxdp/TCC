def maiores(lista,n):
    """Dada uma lista de numeros inteiros e um numero inteiro n,
retorna outra lista contendo todos os numeros da lista
original maiores que n.
list, int->list"""
    lista.append(n)
    list.sort(lista)
    list.index(lista,n)
    return lista[n-1:]