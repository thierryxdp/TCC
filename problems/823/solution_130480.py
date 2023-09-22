def faltante(l):
    n=len(l)
    i=0
    f=0
    l2=[0:n+2]
    
    while i<len(l2):
        if l2[i] not in l:
            f = f + l2[i]
        i=i+1
    return f