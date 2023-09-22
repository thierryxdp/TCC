def maiores (lista,n):
    '''Retorna os números da lista maiores que n, list, int -> list'''
    lista = list (filter(>n))
    return sorted (lista)