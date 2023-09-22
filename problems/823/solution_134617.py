def faltante(L):
    i = 0 
    list.sort(L)
    while i+1<len(L):
        if L[0] != 1:
            return 1
        if L[i+1] != L[i]+1:
            return L
        i+=1