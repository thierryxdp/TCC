def filtra_pares(M):
    """filtra a tupla da entrada retornando uma tupla apenas
    com os pares"""
    M = (a,b,c,d)
    A = a%2
    B = b%2
    C = c%2
    D = d%2
    return (A == 0,B == 0,C == 0,D == 0)