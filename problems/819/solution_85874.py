def filtraMultiplos(t, n):
    """Dado uma lista e um número n, a função filtra os multiplos
    do número n,  e retorna uma lista com esses números.
    Assinatura: list, int --> list
    """
    multiplos= ()
    proximo= 0
    while proximo <len(t):
        if t[proximo]% (n) == 0:
            multiplos = multiplos + (t[proximo],)
        proximo = proximo +1
    return list(multiplos)