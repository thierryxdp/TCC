def maiores(lista,n) :
    """Dada uma lista de números interiros e um número inteiro
    n, retorna outra lista que contém todos os números da lista
    original maiores que n;
    list -> list"""
    x = list.sort(lista)
    w = list.extend(x, n)
    y = list.index(lista,n)
    return lista[y:]