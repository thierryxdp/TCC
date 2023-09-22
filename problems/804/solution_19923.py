def par(x):
    """Funcao que identifica se um numero e par
    int--> bool"""
    if x % 2 == 0:
        return True
    else:
        return False
def filtra_pares(tupla):
    """Funcao que dada uma tupla com 4 elementos retorne apenas
    os numeros pares contidos nela
    tuple-->tuple"""
    w = tupla[0]
    x = tupla[1]
    y = tupla[2]
    z = tupla[3]
    a = ()
    if par(w):
        a = a + (w,)
    if par(x):
        a = a + (x,)
    if par(y):
        a = a + (y,)
    if par(z):
        a = a + (z,)
    return a