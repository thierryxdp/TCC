def quebra_cabeca(L):
    """Essa funcao retorna o numero faltante numa sequencia dada como entrada
    list -> int
    """

    i = 0
    n = 0

    list.sort(L)
    while i < len(L):
        if L[i+1] - L[i] != 1:
            return L[i]+1
    i = i + 1