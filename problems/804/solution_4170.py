def filtra_pares(t):
    t1=[]
    for x in t:
        if x%2==0:
            t1.append(x)
    t2=tuple(t1)        
    return t2