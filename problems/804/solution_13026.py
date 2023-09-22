def n_par(x):
    return (x%2) == 0
def n_impar(x):
    return not n_par(x)
def filtra_pares(a):
    """Recebe uma tupla com quatro elementos e retorna apenas os números
    pares.
    tuple -> tuple"""
    rt = ()
    if n_par(a[1]):
        rt + (a[1],)
    if n_par(a[2]):
        rt + (a[2],)
    if n_par(a[3]):
        rt + (a[3],)
    if n_par(a[4]):
        rt + (a[4],)
        return rt