def maiores(lista,n) :
    """Dada uma lista de números interiros e um número inteiro
    n, retorna outra lista que contém todos os números da lista
    original maiores que n;
    list -> list"""
    z = lista[:]
    list.sort(lista)
    list.extend(x,[n])
    list.index(lista,n)
    y = lista 
    return z[y:]