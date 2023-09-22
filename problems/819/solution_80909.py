def filtraMultiplos(lista, n):
    """Devolve os múltiplos de um número (n), dentro de uma lista de números"""
    i = 0
    mults = ()
    prox = 0
    while i < len(lista):
        if lista[prox] % n == 0:
            mults = mults + (lista[prox],)
        i = i + 1
            prox = prox + 1
    return mults