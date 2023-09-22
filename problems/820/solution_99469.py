def posLetra(texto,l,n):
    i=0
    j=0
    if str.count(texto,l)<n:
        return -1
    
    while j<=n:
        if texto[i]==l:
            j=j+1
        i=i+1
    return j