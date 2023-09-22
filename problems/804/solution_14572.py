def filtra_pares(x):
    """retorna apenas os elementos pares dos 4 parametros
    de uma tupla.
    int, int, int, int -> tuple"""
    if x[0]%2==0:
        tup=tup+(x[0],)
    if x[1]%2==0:
        tup=tup+(x[1],)
    if x[2]%2==0:
        tup=tup+(x[2],)
    if x[3]%2==0:
        tup=tup+(x[3],)
    return tup