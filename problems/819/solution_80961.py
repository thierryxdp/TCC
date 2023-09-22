def filtraMultiplos(lista, n):
    """Devolve os múltiplos de um número (n), dentro de uma lista de números"""
    i = 0
    mults = ()
    while i < len(lista):
        if lista[i] % n == 0:
            mults = mults + (lista[i],)
        i = i + 1
    l1 = list(mults)
    return l1