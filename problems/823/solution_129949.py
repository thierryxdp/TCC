def faltante(L):
    list.sort(L)
    inteiros = list(range(L[-1] + 2))
    del inteiros[0]
    i = 0
    while (inteiro[i] == L[i]):
        i = i + 1
    return inteiro[i]