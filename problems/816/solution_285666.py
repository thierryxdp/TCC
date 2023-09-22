def maiores(lista,n):
    """Função que dada uma lista de números inteiros e um número n, retorna somente números maiores a n"""
    """int--->int"""
    list.append(lista,n)
    list.sort(lista)
    p=list.index(lista,n)
    return lista[p:]