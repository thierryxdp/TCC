def faltante(l):
    i=0
    a=list(range(len(l)+2))[1:]
    
    while i<len(l):
        if a[i]!=l[i]:
            falta=a[i]
        i=i+1
    return falta