def maiores(lista,n) :
    """Dada uma lista de números interiros e um número inteiro
    n, retorna outra lista que contém todos os números da lista
    original maiores que n;
    list -> list"""
    list.extend(lista,[n])
    list.sort(lista)
    y = list.index(lista,n)
    
    return lista[y+1:]