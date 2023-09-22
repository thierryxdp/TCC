def filtraMultiplos(lista, n):
    """Devolve os múltiplos de um número (n), dentro de uma lista de números"""
    i = 0
    mults = ()
    l1 = lista
    while i < len(lista):
        if l1(i) % n == 0:
            mults = mults + (l1(i),)
        i = i + 1
    return mults