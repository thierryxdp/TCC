def faltante(L):
    list.sort(L)
    inteiros = list(range(L[-1]))
    i = 0
    while (i < len(L)):
        if (inteiros[i] != L[1]):
        i = i + 1
    return inteiros[1]