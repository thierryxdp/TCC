def faltante(L):
    i = 0
    while i < len(L):
        if L[0] != 1:
            return 1
        elif len(L) == L[-1]:
            return L[-1]+1
        elif (L[i] != L[i+1]-1):
            return L[i]+1
        i = i+1