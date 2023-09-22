def filtra_pares(tuple):
    """Dado uma tupla com quatro elementos inteiros como parâmetro,
    retorna apenas os elementos pares dessa tupla, na mesma ordem;
    tuple->tuple"""
    return tuple(tuple%2)