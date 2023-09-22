def faltante(L):
    i = 0
    opa = sorted(L)
    while i < len(L):
        if L[i] != opa[i]:
            return L[i] + 1
        i = i + 1