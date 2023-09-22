def filtraMultiplos(l,n):
    r=[]
    for x in l:
        if x%n==0:
            r.append(x) # = list.append(r,x)
    return r