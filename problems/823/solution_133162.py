def faltante(L):
    a = 0
    L1 = L[:]
    contagem = 0
    while contagem < len(L1):
        if (L[0] + 1) == L[1]:
            del L[0]
        else:
            a = L[1] - 1
    return a