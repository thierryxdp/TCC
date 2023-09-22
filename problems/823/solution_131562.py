def faltante(L):
    list.sort(L)
    i=0
    while (i < len(L)+1):
        if (L[i]!=L[i+1]+1):
            x=L[i]+1
        i=i+1
    return x