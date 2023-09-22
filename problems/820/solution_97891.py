def posLetra(f,l,ocorrencia):
    i= 0
    c= 0
    while i<len(f) and c<ocorrencia:
        if f[i]==l:
            c=c+1
        i=i+1
    if c<ocorrencia:
        return -1
    else: 
        return i-1