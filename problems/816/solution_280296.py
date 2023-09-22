def maiores(lista,n) :
    """Dada uma lista de números interiros e um número inteiro
    n, retorna outra lista que contém todos os números da lista
    original maiores que n;
    list -> list"""
    z = lista[:]
    list.sort(lista)
    list.extend(lista,[n])
    y = list.index(lista,n)
    
    return z[y:]