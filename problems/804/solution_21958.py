#Start your python function here
def imparpar(x):
    """Função que retorna se x é ímpar ou par"""
    if x%2 == 0:
        return 'par'
    else:
        return 'ímpar'

def filtra_pares(a, b, c, d):
    """Função que retorna os elementos pares da tupla
    tupla -> tupla"""
    if imparpar(a)=='par' and imparpar(b)=='par' and imparpar(c)=='par' and imparpar(d)=='par':
        return a, b, c, d
    elif imparpar(a)=='par' and imparpar(b)=='par' and imparpar(c)=='par' and imparpar(d)=='ímpar':
        return a, b, c
    elif imparpar(a)=='par' and imparpar(b)=='par' and imparpar(c)=='ímpar' and imparpar(d)=='ímpar':
        return a, b
    elif imparpar(a)=='par' and imparpar(b)=='ímpar' and imparpar(c)=='ímpar' and imparpar(d)=='ímpar':
        return a
    elif imparpar(a)=='ímpar' and imparpar(b)=='ímpar' and imparpar(c)=='ímpar' and imparpar(d)=='ímpar':
        return ()
    elif imparpar(a)=='ímpar' and imparpar(b)=='par' and imparpar(c)=='ímpar' and imparpar(d)=='ímpar':
        return b
    elif imparpar(a)=='ímpar' and imparpar(b)=='par' and imparpar(c)=='par' and imparpar(d)=='ímpar':
        return b, c
    elif imparpar(a)=='ímpar' and imparpar(b)=='par' and imparpar(c)=='par' and imparpar(d)=='par':
        return b, c, d
    elif imparpar(a)=='ímpar' and imparpar(b)=='ímpar' and imparpar(c)=='par' and imparpar(d)=='ímpar':
        return c
    elif imparpar(a)=='ímpar' and imparpar(b)=='ímpar' and imparpar(c)=='par' and imparpar(d)=='par':
        return c, d
    elif imparpar(a)=='par' and imparpar(b)=='ímpar' and imparpar(c)=='par' and imparpar(d)=='ímpar':
        return a, c
    elif imparpar(a)=='par' and imparpar(b)=='ímpar' and imparpar(c)=='ímpar' and imparpar(d)=='par':
        return a, d
    else:
        return b, d