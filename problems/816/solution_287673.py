def maiores (lista,n):
    '''Retorna os números da lista maiores que n, list, int -> list'''
    lista = list (filter(lambda x: x>n, lista))
    return sorted (lista)