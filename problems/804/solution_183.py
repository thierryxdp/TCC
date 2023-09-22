def filtra_pares(tup):
    """Recebe uma tupla com 4 inteiros e retorna uma nova tupla apenas com os números pares; tuple -> tuple"""
    n1, n2, n3, n4=tup
    if n1%2==0:
        return n1
    if n2%2==0:
        return n2
    if n3%2==0:
        return n3
    if n4%2==0:
        return n4
    else:
        return