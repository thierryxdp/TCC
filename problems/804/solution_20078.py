def par(n):
    return n % 2 == 0

def filtra_pares(t):
    """Recebe uma tupla de 4 elementos, e retorna somente os que são pares.
    Testes: filtra_par((1,3,7,9)) == ()
    filtra_par((2,8,6,10)) == (2,8,6,10)
    Assinatura: tuple --> tuple
    """
    ret = ()
    if par(t[0]):
        ret = ret + (t[0], )
    if par(t[1]):
        ret = ret + (t[1], )
    if par(t[2]):
        ret = ret + (t[2], )
    if par(t[3]):
        ret = ret + (t[3], )
    return ret