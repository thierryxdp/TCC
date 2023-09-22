def faltante(L):
    list.sort(L)
    i=0
    while (i < len(L)):
        if (L[i-1]!=L[i]+1):
            x=L[i]+1
            break
        i=i+1
    return x