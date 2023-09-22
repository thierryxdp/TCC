def faltante(L):
    list.sort(L)
    inteiros = list(range(L[-1] + 1))
    del inteiros[0]
    i = 0
    if (inteiros == L):
		return L[-1] + 1
    else:
        while (inteiros[i] == L[i]):
            i = i + 1
        return inteiros[i]