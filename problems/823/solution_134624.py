def faltante(L):
    i = 0 
    N = len(L) + 1
    list.sort(L)
    if L[0] != 1:
        return 1
    if L[-1]<N:
        return N
    while i+1<len(L):
        if L[i+1] != L[i]+1:
            return L[i]+1
        i = i+1