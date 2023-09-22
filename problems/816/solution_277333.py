def maiores(lista,n):
    """Função maiores que, dada uma lista de números inteiros e um número
    inteiro n, retorna outra lista, que contenha todos os números da lista
    original maiores que n.
    lista,int -> lista
    """
    n1=[n]
    lista2 = lista+n1
    lista2.sort()
    x = lista2.index(n)
    y = lista2[x+1:]
    return y