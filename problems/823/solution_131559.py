def faltante(L):
    list.sort(L)
    i=1
    while i<len(L):
        if ( L[i-1]!=L[i]+1):
            x=L[i-1]+2
        i=i+1
    return x