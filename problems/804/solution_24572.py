def filtra_pares (s): 
    l=[]
    for x in s:
        if x%2==0:
            l.arrend(x)
    return tuple(l)