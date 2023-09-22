def faltante(l):
    i=0
    f=0
    l2=list(range(1,len(l)+2))
    
    while i<len(l)+1:
        if l2[i] not in l:
            f = f + l2[i]
        i=i+1
    return f