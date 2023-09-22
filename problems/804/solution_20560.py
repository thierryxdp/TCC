def resto(a, b):
    return a%b

def eh_par(n):
    return resto(n, 2) == 0

def filtra_pares(t):
    """Dada uma tupla com quatro números inteiros, retorna 
    nova tupla apenas com os elementos pares, na mesma ordem
    apresentada no parâmetro.
    assinatura: tuple --> tuple
    testes:
    filtra_pares((1, 2, 3, 4)) == (2, 4)
    filtra_pares((12, 13, 14, 15)) == (12, 14)
    filtra_pares((-1, 0, 1, 2)) == (0, 2)
    """
    ret = ()
    if eh_par(t[0]):
        ret = ret + (t[0], )
    if eh_par(t[1]):
        ret = ret + (t[1], )
    if eh_par(t[2]):
        ret = ret + (t[2], )
    if eh_par(t[3]):
        ret = ret + (t[3], )
    return ret