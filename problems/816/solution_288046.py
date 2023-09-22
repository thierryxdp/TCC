def maiores(lista, n):
    """funçao que retorna uma lista em ordem crescente e um
    a partir de um numero(n) específico, dada uma lista e um numero como entrada"""
    lista.append(lista,n)
    lista.sort(lista)
    return lista[(list.index(lista, n)+1): ]