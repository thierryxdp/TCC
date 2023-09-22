def n_par(x):
    return (n%2) == 0
def n_impar(x):
    return not n_par(x)
def filtra_pares(a,b,c,d):
    """Recebe uma tupla com quatro elementos e retorna apenas os números
    pares.
    tuple -> tuple"""
    rt = ()
    if n_par(a):
        rt + (a,)
    if n_par(b):
        rt + (b,)
    if n_par(c):
        rt + (c,)
    if n_par(d):
        rt + (d,)
        return rt