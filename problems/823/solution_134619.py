def faltante(L):
    i = 0 
    list.sort(L)
    if L[0] != 1:
            return 1
    while i+1<len(L):
        if L[i+1] != L[i]+1:
            return L[i+1]
        i+=1