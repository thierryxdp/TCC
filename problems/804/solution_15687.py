def filtra_pares(a):
    """Filtra uma tupla de quatro elementos inteiros retornando uma nova tupla apenas com os elementos pares
    da tupla fornecida.
    tuple -> tuple"""
    tup=()
    if a[0]%2==0:
        tup=tup+(a[0],)
    if a[1]%2==0:
        tup=tup+(a[1],)
    if a[2]%2==0:
        tup=tup+(a[2],)
    if a[3]%2==0:
        tup=tup+(a[3],)
    return tup