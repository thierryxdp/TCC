def e_par(t):
    """Retorna um bool que garante se um inteiro t é par ou não
    int -> bool"""
    return t%2 == 0
    
def filtra_pares(t):
    """Retorna uma tupla contendo os elementos pares na mesma
    ordem da tupla original.
    tupla -> tupla"""
    ret = ()
    if e_par(t[0]):
        ret += (t[0],)
    if e_par(t[1]):
        ret +=(t[1],)
    if e_par(t[2]):
        ret += (t[2],)
    if e_par(t[3]):
        ret += (t[3],)
    return ret

# Casos de teste:
# filtra_pares((0,0,0,0)) == (0,0,0,0)
# filtra_pares((1,2,3,4)) == (2,4)
# filtra_pares((-2,3,13,34)) == (-2,34)
# filtra_pares((3,7,9,1)) == ()