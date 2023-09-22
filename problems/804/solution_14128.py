def e_par (t):
    """ verifica se um numero é par."""
    if t%2 == 2:
        return true
def filtra_pares (t):
    ret = ()
    if e_par (t[0]):
        ret = ret + (t[0],)
    if e_par (t[1]):
        ret = ret + (t[1],)
    if e_par (t[2]):
        ret = ret + (t[2],)
    if e_par (t[3]):
        ret = ret + (t[3],)
    return ret