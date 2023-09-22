def faltante(L):
    list.sort(L)
    i=0
    while (i <= len(L)):
        if (L[i]!=L[i+1]+1):
            x=L[i]+1
        i=i+1
    return x