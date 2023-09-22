def e_par(t):
    """Retorna um bool que garante se um inteiro t é par ou não
    int -> bool"""
    return t%2 == 0
    
def filtra_pares(t1,t2,t3,t4):
    """Retorna uma tupla contendo os elementos pares na mesma
    ordem da tupla original.
    tupla(int, int, int, int) -> tupla"""
    ret = ()
    if e_par(t1):
        ret += (t1,)
    if e_par(t2):
        ret +=(t2,)
    if e_par(t3):
        ret += (t3,)
    if e_par(t4):
        ret += (t4,)
    return ret

# Casos de teste:
# filtra_pares(0,0,0,0) == (0,0,0,0)
# filtra_pares(1,2,3,4) == (2,4)
# filtra_pares(-2,3,13,34) == (-2,34)