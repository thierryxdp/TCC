def faltante(L):
    """Determinar o numero que resta na sequencia da lista;
    list -> int"""
    x = 0
    N = 1
    faltou = len(L) + 1
    while x < len(L):
        if L[x] != N:
            faltou = N
            break
        N += 1
        x += 1
    return faltou