def filtra_pares(tupla):
    """essa função tem como entrada quatro elementos em formato tuple
    e retorna apenas os que são pares, na mesma ordem em que estavam inicialmente;
    tuple,tuple,tuple,tuple---->tuple"""
    lista1 = [tupla]
    lista2 = sorted(filter(lambda x: x%2 == 0, lista1))
    return lista2