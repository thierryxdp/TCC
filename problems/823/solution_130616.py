def faltante(l):
    i=0
    a=list(range(len(l)+2))[1:]
    b=list(range(l[-1]+1))[1:1]
    
    while i<len(l):
        if l in a:
            falta=len(l)+1
        elif l[i]!=a[i]:
            falta= a[i]
    i=i+1
    return falta