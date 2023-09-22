def n_par(x):
    return (x%2) == 0
def n_impar(x):
    return not n_par(x)
def filtra_pares(a):
    """Recebe uma tupla com quatro elementos e retorna apenas os números
    pares.
    tuple -> tuple"""
    ret = ()
    if n_par(a[0]):
       ret = ret + (a[0],)
    if n_par(a[1]):
       ret = ret + (a[1],)
    if n_par(a[2]):
       ret = ret + (a[2],)
    if n_par(a[3]):
       ret = ret + (a[3],)
        return ret